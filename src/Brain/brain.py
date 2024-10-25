from openai import OpenAI
import random
from src.consts import *
import src.models as models
from src.utils import create_personality_prompt
from rich import print
from colorama import Fore



class Brain:
    def __init__(self, name=None, personality=None, age=None, parents=None,current_location=None,birthplace=None,work=None,working=None,friends=None,enemies=None,memory=None,emotion=None,short_term_memory=None,acquaintances=None,memory_quality=None):
        self.openai = OpenAI(api_key=API_KEY, base_url=API_URL)
        self.completion = self.openai.beta.chat.completions.parse

        # Characteristic of the AI
        self.name = name if name else random.choice(RANDOM_NAMES)
        self.personality = (
            personality
            if personality
            else [
                random.choice(RANDOM_PERSONALITIES)
                for _ in range(NUMBER_OF_PERSONALITIES)
            ]
        )
        self.id = random.randint(0, 1000000)
        self.age = age if age else 18
        self.parents: list[models.Parent] = parents if parents else []

        self.birthplace = birthplace if birthplace else None
        self.current_location = current_location if current_location else birthplace if birthplace else None
        self.work = work if work else random.choice(RANDOM_WORKS)
        self.working = working if working else False
        self.friends = friends if friends else []
        self.enemies = enemies if enemies else []
        self.memory = memory if memory else set()
        self.emotion = emotion if emotion else "neutral"
        self.short_term_memory = short_term_memory if short_term_memory else []
        self.acquaintances = acquaintances if acquaintances else []
        self.initial_prompt = create_personality_prompt(self)
        self.memory_quality = memory_quality if memory_quality else 20  # memoria de corto plazo maxima
        self.want_to_talk = True

    def get_memory(self) -> str:
        return ", ".join(self.memory)

    def talk(self, text: str) -> str:
        response = self.think(text)

        self.short_term_memory_add(
            models.Dialog(role="assistant", content=response.respuesta)
        )
        return response.respuesta

    def short_term_memory_add(self, dialog: models.Dialog) -> str:
        if len(self.short_term_memory) > self.memory_quality:
            self.short_term_memory.pop(0)
        self.short_term_memory.append(
            {
                "role": dialog.role,
                "content": dialog.content,
            }
        )

    def think(self, text: str):
        self.short_term_memory_add(models.Dialog(role="user", content=text))
        new_short_memory = self.short_term_memory.copy()
        # System Prompt
        new_short_memory.insert(
            0, models.Dialog(role="system", content=self.initial_prompt)
        )
        # Memory Prompt
        new_short_memory.insert(
            len(self.short_term_memory),
            models.Dialog(
                role="system",
                content="Recuerdos Importantes: "
                + (self.get_memory() if len(self.memory) > 0 else "No hay"),
            ),
        )
        # Emotion Prompt
        new_short_memory.append(
            models.Dialog(role="system", content=f"Emocion actual: {self.emotion}"),
        )
        # Personal Prompt
        new_short_memory.append(
            models.Dialog(
                role="system",
                content=f"Tus datos {str(self)}"
            ),
        )
        response = self.completion(
            model=MODEL,
            messages=new_short_memory,
            response_format=models.ResponseFormat
        )
        parsed = response.choices[0].message.parsed
        # Log
        print({
            "action": parsed.action,
            "action_data": parsed.action_data,
            "respuesta": parsed.respuesta,
            "Emocion actual": parsed.emocion_actual
        },)
        # Compruebo si hay una accion a realizar
        if parsed.action_data and not parsed.action_data.strip() == "":
            if parsed.action == "remember":
                self.remember(parsed.action_data)
            elif parsed.action == "add_acquaintance":
                self.acquaintances.append(parsed.action_data)
            elif parsed.action == "leave":
                self.want_to_talk = False
        # Compruebo si a cambiado la emocion
        if parsed.emocion_actual and not parsed.emocion_actual.strip() == "":
            if parsed.emocion_actual != self.emotion:
                print(f"◆Ahora {self.name} se siente {parsed.emocion_actual}◆")
            self.emotion = parsed.emocion_actual
        return parsed

    def remember(self, memory: str) -> None:
        self.memory.add(memory)

    def forget(self, memory: str) -> None:
        self.memory.remove(memory)
    
    def basic_info(self):
        return f"{self.name} es un {self.work} de {self.age} años, nacido en {self.birthplace}, actualmente en {self.current_location}."
    
    def __str__(self):
        return f"name={self.name}, personality={self.personality}, age={self.age}, parents={self.parents}, birthplace={self.birthplace}, work={self.work}, working={self.working}, friends={self.friends}, enemies={self.enemies}, memory={self.memory}, emotion={self.emotion}, short_term_memory={self.short_term_memory}, acquaintances={self.acquaintances}"