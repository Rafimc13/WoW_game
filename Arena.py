import copy
import random
from Character import *


class Arena:

    def __init__(self, teamA, teamB):
        self.team_A = teamA
        self.team_B = teamB

    def print_state(self):
        print("State of Characters team A are: ")
        for character in self.team_A:
            character.print()
        print("\nState of Characters team B are: ")
        for character in self.team_B:
            character.print()



    def play (self):
        time = -1
        my_teamA = []
        my_teamB = []
        while True:
            # print(len(my_teamA))
            # print(len(my_teamB))
            time+=1
            print("Round: " + str(time))
            print("---" * 20)
            my_teamA.clear()
            my_teamB.clear()
            for character in self.team_A:
                character.print()
                if character.is_dead():
                    self.team_A.remove(character)
                elif character.delay == 0:
                    my_teamA.append(character)
                else:
                    character.end_round()
            for character in self.team_B:
                character.print()
                if character.is_dead():
                    self.team_B.remove (character)
                elif character.delay ==0:
                    my_teamB.append(character)
                else:
                    character.end_round()

            if len(self.team_A)==0:
                if len(self.team_B)>0:
                    print ("Team B won the GAME!!")
                    break
                else:
                    print("We have a TIE.")
                    break
            elif len(self.team_B)==0:
                print("Team A won the GAME!!")
                break
            for character in my_teamA:
                c = self.team_B[randrange(len(self.team_B))]
                c.health = c.health - character.attack()
                character.end_round()
            for character in my_teamB:
                c2 = self.team_A[randrange(len(self.team_A))]
                c2.health = c2.health - character.attack()
                character.end_round()







