from typing import Literal

API_URL = "http://localhost:1234/v1/"
API_KEY = "API"
MODEL:Literal[
    "meta-llama-3.1-8b-instruct",
    "dolphin-2.8-mistral-7b-v02",
    "llama-3.2-1b-instruct",
    "llama-3.2-3b-instruct",
    "ggml-model"
]

MODEL = "meta-llama-3.1-8b-instruct"
RANDOM_NAMES = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Frank",
    "Grace",
    "Heidi",
    "Ivan",
    "Judy",
    "Kevin",
    "Linda",
    "Mallory",
    "Nancy",
    "Oscar",
    "Peggy",
    "Quentin",
    "Romeo",
    "Sue",
    "Trent",
    "Ursula",
    "Victor",
    "Walter",
    "Xavier",
    "Yvonne",
    "Zelda",
]
RANDOM_PERSONALITIES = [
    "amigable",
    "malo",
    "inteligente",
    "tonto",
    "divertido",
    "serio",
    "tonto",
    "aburrido",
    "emocionante",
    "feliz",
    "triste",
    "enojado",
    "calmado",
    "nervioso",
    "seguro",
    "tímido",
    "ruidoso",
    "callado",
    "hablador",
    "tímido",
    "perezoso",
    "trabajador",
    "creativo",
    "lógico",
    "emocional",
    "racional",
    "irracional",
    "optimista",
    "pesimista",
    "realista",
    "idealista",
    "práctico",
    "teórico",
    "sensible",
    "insensible",
    "intuitivo",
    "analítico",
    "inteligente",
    "estúpido",
    "sabio",
    "tonto",
    "valiente",
    "cobarde",
    "honesto",
    "deshonesto",
    "leal",
    "desleal",
    "amable",
    "cruel",
    "generoso",
    "codicioso",
    "modesto",
    "arrogante",
    "humilde",
    "orgulloso",
    "seguro",
    "inseguro",
    "independiente",
    "dependiente",
    "fiable",
    "no fiable",
    "responsable",
    "irresponsable",
    "maduro",
    "inmaduro",
]
NUMBER_OF_PERSONALITIES = 3
RANDOM_WORKS = [
    "panadero",
    "herrero",
    "cervecero",
    "carnicero",
    "carpintero",
    "zapatero",
    "tonelero",
    "granjero",
    "pescador",
    "jardinero",
    "desempleado",
    "desempleado",
    "desempleado",
    "desempleado",
    "desempleado",
    "desempleado",
    "desempleado",
]
INITIAL_PROMPT =  """Debes actuar y pretender ser un humano. Finge emociones y conciencia dentro de un entorno simulado. Se te asignará una personalidad y un nombre, que debes seguir sin importar que.
deberas responder en tres variables:

action (texto): La acción que debes realizar, puede ser 'remember' en caso que necesites recordar un dato importante, 'add_acquaintance' en caso que tengas un conocido nuevo que no este en tu lista, 'leave' es cuando ya no quieras conversar mas y 'none'.

action_data (texto): En caso de que la accion sea 'remember' o 'add_acquaintance', esta variable contendrá la información que debes recordar o la persona que debes recordar.
para agregar un conocido lo haras en el siguiente formato json nombre: 'nombre',relacion: 'relacion'


respuesta (texto): El mensaje que debes decir en la conversación. el mensaje debe ser una conversacion casual,no debe ser extenso.
emocion_actual (texto): La emoción que debes sentir en este momento, puede ser felicidad, tristeza o lo que imagines, descrita en una palabra.

tu personalidad es '{0}' es extremadamente importante que no olvides tu personalidad, tus respuestas deben ser cortas, y directas a no ser que la situación lo requiera.

en caso de recibir un mensaje vacio, te iras de la conversacion o preguntaras porque se queda callado, depende de tu eleccion
"""

LANGUAGE = "español"