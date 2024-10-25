from src.Brain import Brain
from src.utils import create_personality_prompt
from src.models import Parent
from rich import print
import sys
check_personality = False


current_location = "ESTADOS UNIDOS"

def ia_conversation(p1:Brain,p2:Brain):

    c = 0
    r2 = "Hola"
    while c <= 10:
        r1 = p1.talk(r2)
        print(f"{p1.name}: {r1}")
        print()
        r2 = p2.talk(r1)
        print(f"{p2.name}: {r2}")
        print()
        c +=1
        if p1.want_to_talk == False or p2.want_to_talk == False:
            break
        if c > 10:
            if input("Want continue?") == "y":
                c = 0
    print(p1.get_memory())
    print(p2.get_memory())
    
def conversation(ia:Brain):
    print(f"Hablaras con {ia.name}")
    pronoun = "Ella" if ia.name[-1] == "a" else "El"
    print(f"{pronoun} tiene {ia.age} años")
    print(f"Personalidad: {ia.personality}")
    print()
    
    while True:
        m = input("tu: ")
        print()
        if m == "-m":
            print(ia.get_memory())
            print()
        elif m == "-q":
            sys.exit()
        else:
            response = ia.talk(m)
            print(f"{ia.name}: {response}")
            print()

giselle = Brain(
    name="Giselle",
    age=20,
    birthplace="Santiago, Chile",
    work="Psicologa",
    current_location=current_location,
    parents=[
        Parent(name="Juan Perez",relationship="padre"),
        Parent(name="Maria Perez",relationship="madre")
    ],
    personality=[
        "perseverante", "intuitivo", "egoista", "egocentrico"
    ]
)

matias = Brain(
    name="Matias",
    age=20,
    personality=[
        "perseverante", "intuitivo", "egoista", "egocentrico"
    ],
    birthplace="Temuco, Chile",
    work="Estudiante",
    current_location=current_location,
    parents=[
        Parent(name="Juan Perez",relationship="padre"),
    ]
)

# ia_conversation(brain,matias)
conversation(giselle)
