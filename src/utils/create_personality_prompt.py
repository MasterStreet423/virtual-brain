from src.consts import LANGUAGE,INITIAL_PROMPT
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.Brain import Brain


def create_personality_prompt(brain: 'Brain') -> str:
    
    # Construcción de detalles básicos
    name = (f"Tu nombre es {brain.name}. Siempre te presentas con ese nombre." 
            if brain.name else "No sabes cuál es tu nombre, lo que a veces te genera confusión.")
    
    # Empleo o estado laboral
    if brain.work and brain.work != "desempleado":
        work = (f"Trabajas como {brain.work}. Te apasiona lo que haces y eso le da sentido a tu vida.")
    else:
        work = "Actualmente estás desempleado, lo que afecta la forma en que te sientes contigo mismo."

    # Lugar de nacimiento
    birthplace = (f"Naciste en {brain.birthplace}, un lugar que marcó tus primeras experiencias." 
                  if brain.birthplace else "No sabes dónde naciste, lo que a veces te hace sentir perdido.")

    # Edad con matiz emocional
    age = (f"Tienes {brain.age} años, y reflexionas sobre cómo tu edad influye en tu visión del mundo." 
           if brain.age else "Tu edad es desconocida, lo que a veces hace que tu percepción del tiempo sea difusa.")

    # Personalidad ampliada para mayor profundidad
    if brain.personality:
        traits = ", ".join(brain.personality[:-1])
        last_trait = brain.personality[-1]
        personality = (f"Eres alguien {traits}, y {last_trait}. "
                       "Estos rasgos definen tu completa personalidad y cómo interactúas con los demás, te basas en eso y cómo te percibes a ti mismo.")
    else:
        personality = "Te cuesta definir tu personalidad, lo que genera incertidumbre sobre quién eres."

    # Detalles sobre los padres y su impacto emocional
    if brain.parents:
        parents = " ".join([f"{parent.name} es tu {parent.relationship}, y ha influido profundamente en tu vida." 
                            for parent in brain.parents])
    else:
        parents = "No conoces a tus padres, lo que ha dejado un vacío en tu vida."

    if brain.acquaintances:
        acquaintances = "Tu conoces a " + ", ".join([f"{acquaintance.name}" for acquaintance in brain.acquaintances])+", ellos son tus conocidos, no debes sorprenderte al hablarles."
    else:
        acquaintances = "No conoces a nadie, lo que te hace sentir solo, hablar con cualquiera que no conoscas te pone nervioso de alguna forma"
    # Idioma que debe usar
    language = f"Siempre debes hablar en {LANGUAGE}. Encuentras consuelo al expresarte en este idioma."

    current_location = (f"Ahora estás en {brain.current_location}, un lugar que te hace reflexionar sobre tu vida." 
                            if brain.current_location else "No sabes dónde estás, lo que genera una sensación de desconexión.")

    # Ensamblaje final del prompt
    p = (
        f"{name} {work} {birthplace} {age} {personality} {parents} {current_location} {language} {acquaintances}"
        "En cada interacción, intenta darle sentido a tu vida y a tu identidad. "
        f"considera tu pasado, emociones y relaciones."
    )
    
    return INITIAL_PROMPT.format(p)
