from src.Brain import Brain
from src.utils import create_personality_prompt

b = Brain(
    name="Franca",
    personalities=["divertida", "inteligente", "pervertida"],
    age=23
)

print(f"Hablaras con {b.name}")
print(f"{"Ella" if b.name[-1] == "a" else "El"} tiene {b.age} años")
print(f"Personalidad: {b.personality}")
print()

while True:
    r = input("You: ")
    print(b.name+":",b.talk(r))