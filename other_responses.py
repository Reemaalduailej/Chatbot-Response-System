
import random

R_RECOMMEND = "I would recommend going for a walk or maybe you can practice your favorite hobby :)"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_WATER_INTAKE = "Your preferable water intake in liters equals your weight in kg multiplied by 0.033"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response
