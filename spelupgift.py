import random

class spelare:
    def __init__(self, namn):
        self.__namn = namn
        self.__monster

class monster:
    def __init__(self):
        namn = namn
        hp = hp
        attack = attack

    def pss(self):
        print(self.namn, self.hp, self.attack)

    def slå(self):
        return random.randint(1, self.attack)

class drake(monster):
    def __init__(self):
        super().__init__("Drake", 30, 8)