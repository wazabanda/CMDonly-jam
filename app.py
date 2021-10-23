import time
import os
from pytimedinput import timedKey
from colorama import *
from entity import *
import pyfiglet


#? main stuff
GAMELOOPSPEED = 1



Entities = []

player = entity("@ ",0,0,1)
Entities.append(player)
#? a short intro
introBanner = pri = pyfiglet.figlet_format("A Game By")
introBanner2 = pri = pyfiglet.figlet_format("waza_Dev")
print(introBanner)
print(introBanner2)
time.sleep(2)
#? an 9X9 board i could have done this in numpy but i did'nt
BOARD = [
    ["* ","* ","* ","* ","* ","* ","* ","* ","* ",],
    ["* ","* ","* ","* ","* ","* ","* ","* ","* ",],
    ["* ","* ","* ","* ","* ","* ","* ","* ","* ",],
    ["* ","* ","* ","* ","* ","* ","* ","* ","* ",],
    ["* ","* ","* ","* ","* ","* ","* ","* ","* ",],
    ["* ","* ","* ","* ","* ","* ","* ","* ","* ",],
    ["* ","* ","* ","* ","* ","* ","* ","* ","* ",],
    ["* ","* ","* ","* ","* ","* ","* ","* ","* ",],
    ["* ","* ","* ","* ","* ","* ","* ","* ","* ",],]
def printBoard():
    printedBoard = ""
    for i in BOARD:
        for j in i:
            printedBoard += j +" "
        printedBoard += "\n"
    return printedBoard

def createEntity(displaySprite,xposition,yposition,deltax,deltay):
    newEntity  = entity(displaySprite,xposition,yposition,deltax,deltay)
    Entities.append(newEntity)
    return newEntity


print(Entities)
while True:
    os.system("cls")
    for i in Entities:
        i.update(BOARD)
        i.render(BOARD)
    print(printBoard())
    #? input 
    userText, timedOut = timedKey(allowCharacters="wasd",timeout=GAMELOOPSPEED)
    if(timedOut):
        continue
    else:
        if userText.lower == "w":
            player.move(0,-1,BOARD)
        elif userText.lower == "s":
            player.move(0,1,BOARD)
        elif userText.lower == "a":
            player.move(-1,0,BOARD)
        elif userText.lower == "d":
            player.move(1,0,BOARD)
    