from Arena import *
from random import randrange


teamA = []
teamB = []

for i in range(5):
    c = Character("orc", 2)
    teamA.append(c)
    teamA[i].delay = randrange(0,4)

for i in range(3):
    c = Character("night elf", 3)
    teamB.append(c)
    teamB[i].delay = randrange(0,3)

WoW_game = Arena(teamA, teamB)
WoW_game.print_state()
WoW_game.play()
