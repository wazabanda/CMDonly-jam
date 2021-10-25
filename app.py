import time
import math
import os
import random
from pytimedinput import timedKey
from colorama import *
from entity import *
from Board import *
import pyfiglet


#? main stuff
GAMELOOPSPEED = 0.25
Playing = True
global player 
global score
global enemyCount
enemyCount = 2
score = 0
# ? every entity in the game is stored here, if it ain't then its as good as destroyed   
Entities = []
minDistance = 2
ENTITYCOUNT = 0
#? a short intro Delete it if you want
introBanner  = pyfiglet.figlet_format("A Game By")
introBanner2  =pyfiglet.figlet_format("waza_Dev")
print(Fore.YELLOW+ introBanner + Fore.WHITE)
print(Fore.BLUE + introBanner2+ Fore.WHITE)
time.sleep(2)
os.system("cls")
print(f"""
    For {Fore.RED} DEVNUGGET'S {Fore.GREEN} CMD only Jam {Fore.WHITE}  
""")
time.sleep(2)
os.system("cls")
print(f"""
    This game was poorly made but here we go

    You are the {Fore.GREEN } @ {Fore.WHITE} and you goal is to get the { Fore.CYAN + Back.CYAN +". "+Fore.WHITE + Back.BLACK}
    to the {Fore.GREEN + Back.GREEN +". "+Fore.WHITE + Back.BLACK} while avoiding the
    {Fore.RED + Back.RED +". "+Fore.WHITE + Back.BLACK}
""")
time.sleep(2)
input(f"{Fore.RED + 'I know this i peak game play' + Fore.WHITE} press any key to continue")
#? an 9X9 board i could have done this in numpy but i did'nt, classes a the boom
BOARD = BOARDclass(10,10)
def printBoard():
    printedBoard = ""
    for i in BOARD.grid:
        for j in i:
            printedBoard += j +" "
        printedBoard += "\n"
    return printedBoard
def addScore():
    global score
    score += 1
def quitGame():
    global Playing
    Playing = False
    End  = pyfiglet.figlet_format("GAME OVER")
    print(f"{Fore.RED} {End} {Fore.WHITE}")
    print (f"{Fore.GREEN + Style.BRIGHT} Final Score : {Fore.WHITE + Style.NORMAL} {score} \n")


def checkEmpties(x,y):
    
    global minDistance
    for i in Entities:
        if i.xPosition == x and i.yPosition == y:
            return False
        ab1 = abs(x-i.xPosition)
        ab2 = abs(y-i.yPosition)
        #        if ab1 < minDistance or  ab2 < minDistance:
        #            return False
    return True
    #Entities.append(player)
def createEntity(displaySprite,xposition,yposition,deltax,deltay,Id,callBack = None):
    x,y =0,0
    while True:
        x = random.randint(0, BOARD.width)
        y = random.randint(0, BOARD.hight)
        if checkEmpties(x,y):
            break
    if xposition == 0 and yposition == 0:
        xposition = x
        yposition = y
    newEntity  = entity(Entities,BOARD,displaySprite,xposition,yposition,deltax,deltay,Id,callBack)  
    Entities.append(newEntity)
    return newEntity
def prepareBoard():
    global Entities
    global player
    global enemyCount
    Entities = []
    player = createEntity(Fore.GREEN + "@ " +Fore.WHITE ,math.floor(BOARD.width/2),math.floor(BOARD.height/2),0,0,"player",quitGame)
    for i in range(enemyCount):
        createEnemy()
    createRigid()
    createGoal()
    
    enemyCount += 1
#? enemyEntity
def createEnemy():

    createEntity(Fore.RED + Back.RED +". "+Fore.WHITE + Back.BLACK,0,0,random.randint(1, 3),random.randint(1, 3),"enemy",quitGame)
#? RigidEntity
def createRigid():
    createEntity(Fore.CYAN + Back.CYAN +". "+Fore.WHITE + Back.BLACK,0,0,0,0,"rigid",prepareBoard)
#? GoalEntity
def createGoal():
    createEntity(Fore.GREEN + Back.GREEN +". "+Fore.WHITE + Back.BLACK,0,0,0,0,"goal",addScore)


#! i could move all these functions to another file but i dont want to 😅
#? if you plan on reusing this to make something just delete or change up these functions excluding print board that one is essential

prepareBoard()

#? gamePlayLoop
while Playing:
    os.system("cls")

    for i in Entities:
        i.update(BOARD,Entities)
        i.render(BOARD)
    if(Playing):
        print (f"{Fore.GREEN + Style.BRIGHT} Score : {Fore.WHITE + Style.NORMAL} {score} \n")
        print(Fore.WHITE + printBoard())

    #? input 
    userText, timedOut = timedKey(allowCharacters="wasdq",timeout=GAMELOOPSPEED)
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
        elif userText == "q":
            break
    time.sleep(GAMELOOPSPEED)
