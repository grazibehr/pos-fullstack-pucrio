# ============================================
# EXERCÍCIO 16 – DIP (DEPENDENCY INVERSION PRINCIPLE)
# --------------------------------------------
# O código deve depender de abstrações, e não das implementações
# ============================================


class Sounds:
    def makes_sound(self):
        pass

class Cat:
    def makes_sound(self):
        return "Miau"
        pass

class Dog:
    def makes_sound(self):
        return "Au"
        pass

class AnimalSpeaker:
    def __init__(self, animal: Sounds):
        self.animal = animal

    def speak(self):
        print(self.animal.makes_sound())                    


# ======================
# TESTANDO
# ======================
if __name__ == "__main__":
    dog_speaker = AnimalSpeaker(Dog())
    dog_speaker.speak()

    cat_speaker = AnimalSpeaker(Cat())
    cat_speaker.speak()        