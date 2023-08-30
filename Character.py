from random import randrange

class Character:

    # def __init__(self, name):
    #     self.name= name
    #     self.health = self.__validate(100, 0, 100)
    #     self.attack_sp = self.__validate(2, 1, 10)
    #     self.delay = 0

    #να έχω την επιλογή να βάλω και attack speed!
    def __init__(self, name, attack_sp):
        self.name= name
        self.health = 100
        self.attack_sp = attack_sp
        self.delay = 0

    # #να έχω επιλογή να τα βάλω όλα σαν χρήστης!!!
    # def __init__(self):
    #     self.name = "example"
    #     self.health = self.__validate(100, 0, 100)
    #     self.attack_sp = self.__validate(2, 1, 10)
    #     self.delay = 0


    def attack (self):
        self.delay = 10 - self.attack_sp
        return randrange(3,11)

    def is_dead (self):
        if self.health<=0:
            return True
        else:
            return False

    def end_round (self):
        if self.health<100:
            self.health+=1
        self.delay = self.delay - 1

    def print (self):
        print(f"name: {self.name}, health: {self.health}, "
              f"attack speed: {self.attack_sp}, delay: {self.delay}")

    def __validate (self, val, lower, upper):
        if val>=lower and val<=upper:
            return val
        else:
            return 0



