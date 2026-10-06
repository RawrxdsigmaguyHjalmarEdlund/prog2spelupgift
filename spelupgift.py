import random

class spelare:
    def __init__(self):
        self.__namn = "namn"
        self.__monster = monster
    def set_namn(self, namn):
        self.__namn = namn

    def set_monsterdrake(self):
        self.__monster = drake()
    
    def set_monsterslime(self):
            self.__monster = slime()

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

intevalt = True
while intevalt == True:
    print(f"{spelare1.hämta_namn()} Tur att välja monster.")
    svar1 = input("tryck 1 för att välja drake och 2 för slime. ")
    if svar1 == "1":
        spelare1.set_monsterdrake
        intevalt = False
    elif svar1 == "2":
        spelare1.set_monsterslime
        intevalt = False

intevalt2 = True
while intevalt2 == True:
    print(f"{spelare2.hämta_namn()} Tur att välja monster.")
    svar2 = input("tryck 1 för att välja drake och 2 för slime. ")
    if svar2 == "1":
        spelare2.set_monsterdrake
        intevalt2 = False
    elif svar2 == "2":
        spelare2.set_monsterslime
        intevalt2 = False