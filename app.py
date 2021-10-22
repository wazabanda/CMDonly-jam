import time
import os
from pytimedinput import timedKey
from colorama import *
from entity import *
#todo 
GAMELOOPSPEED = 1
player = entity("@ ",0,0)
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
while True:
    os.system("cls")
    #? input 
    print(printBoard())
    userText, timedOut = timedKey(allowCharacters="wasd",timeout=GAMELOOPSPEED)
    if(timedOut):
        continue
    else:
        if userText == "w":
            player.move(0,-1,BOARD)
        elif userText == "s":
            player.move(0,1,BOARD)
        elif userText == "a":
            player.move(-1,0,BOARD)
        elif userText == "d":
            player.move(1,0,BOARD)
    