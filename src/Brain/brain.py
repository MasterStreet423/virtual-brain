from openai import OpenAI
import random
from src.consts import *
import src.models as models
from src.utils import create_personality_prompt


class Brain:
    def __init__(self, name=None, personalities=None, age=None):
        self.openai = OpenAI(api_key=API_KEY, base_url=API_URL)
        self.completion = self.openai.beta.chat.completions.parse

        # Characteristic of the AI
        self.name = name if name else random.choice(RANDOM_NAMES)
        self.personality = (
            personalities
            if personalities
            else [
                random.choice(RANDOM_PERSONALITIES)
                for _ in range(NUMBER_OF_PERSONALITIES)
            ]
        )
        self.age = age if age else 18
        self.parents: list[models.Parent] = []

        self.birthplace = None
        self.work = None
        self.working = False
        self.friends = []
        self.enemies = []
        self.memory = []
        self.emotion = "neutral"
        self.short_term_memory = []
        self.initial_prompt = create_personality_prompt(self)
        self.memory_quality = 20  # memoria de corto plazo maxima

    def get_memory(self) -> str:
        return ", ".join(self.memory)

    def talk(self, text: str) -> str:
        response = self.think(text)

        self.short_term_memory_add(
            models.Dialog(role="assistant", content=response.mensaje)
        )
        return response.mensaje

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
        new_short_memory.insert(
            len(self.short_term_memory),
            models.Dialog(role="system", content=f"Emocion actual: {self.emotion}"),
        )
        response = self.completion(
            model=MODEL,
            messages=new_short_memory,
            response_format=models.ResponseFormat,
            max_tokens=150,
        )
        parsed = response.choices[0].message.parsed

        if parsed.necesita_recordar:
            self.remember(parsed.necesita_recordar)
        if parsed.emocion_actual and not parsed.emocion_actual.strip() == "":
            if parsed.emocion_actual != self.emotion:
                print(f"Ahora {self.name} se siente {parsed.emocion_actual}")
            self.emotion = parsed.emocion_actual
        return parsed

    def remember(self, memory: str) -> None:
        self.memory.append(memory)

    def forget(self, memory: str) -> None:
        self.memory.remove(memory)
