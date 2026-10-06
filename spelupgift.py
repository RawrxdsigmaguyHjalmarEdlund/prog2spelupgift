import random

class spelare:
    def __init__(self):
        self.__namn = "namn"
        self.__monster = monster
    def set_namn(self, namn):
        self.__namn = namn

    def set_monster(self, monster):
        self.__monster = monster

    def hämta_namn(self):
        return self.__namn

    def hämta_monster(self):
        return self.__monster
        
class monster:
    def __init__(self, namn, hp, attack):
        self.namn = namn
        self.hp = hp
        self.attack = attack

    def pss(self):
        print(f"{self.namn}: HP {self.hp}, attack {self.attack}")

    def slå(self):
        return random.randint(1, self.attack)

class drake(monster):
    def __init__(self):
        super().__init__("Drake", 30, 8)

class slime(monster):
    def __init__(self):
        super().__init__("slime", 40, 8)

spelare1 = spelare()
spelare2 = spelare()
spelare1.set_namn(input("Vad är spelare 1 namn? "))
spelare2.set_namn(input("Vad är spelare 2 namn? "))

monsterlista = [
    drake(),
    slime()
]

for monster in monsterlista:
    monster.pss()

