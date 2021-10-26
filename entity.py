
# * these are the current ids that i am currently using, just remember
# ? player for player
# ? enemy for enemy
# ? rigid for rigidBodies
# ? goal for goal
# ! just a reminder because of the way the board is printed -1 on the y is up and 1 is down
class entity():
    DisplayText = ""
    xPosition = 0
    yPosition = 0
    deltaX = 0
    deltaY = 0
    destroyOthersCallBack = None
    entityList = []
    
    iD = ""

    def move(self,x,y,board):
        if (x + y > 0) or(x+y < 0):
            self.collision(x,y,board)
            board.grid[self.yPosition][self.xPosition] = board.defultPlaceHolder
            if self.xPosition + x < board.width and self.xPosition + x >= 0:
                self.xPosition += x
            else:
                self.deltaX *= -1
            if self.yPosition + y < board.height and self.yPosition + y >= 0:
                self.yPosition += y
            else:
                self.deltaY *= -1
    """xMove and yMove are used to show the entities direction of movement"""
    def collision(self,xMove,yMove,board):
        for ent in self.entityList:
            if (ent.xPosition == self.xPosition+xMove)and (ent.yPosition == self.yPosition+yMove)and (ent != self):
                if self.iD == "enemy" and ent.iD == "player":
                    ent.destroy()
                elif self.iD == "player" and ent.iD == "goal":
                    continue
                elif self.iD == "rigid" and ent.iD == "goal":
                    ent.collisionCallback()
                    self.collisionCallback()
                elif self.iD == "enemy" and (ent.iD == "rigid" or ent.iD == "goal"):
                    continue
                else:
                    ent.move(xMove,yMove,board)
                break

    def render(self,board):
        board.grid[self.yPosition][self.xPosition] = self.DisplayText
        
    def update(self,board,entityList):
        self.entityList = entityList
        self.render(board)
        self.move(self.deltaX, self.deltaY, board)
    def destroy(self):
        if self.collisionCallback:
            self.collisionCallback()
        self.entityList.remove(self)
    # ! THE INIT METHODE IS KINDA THICC NOW BUT WHO CARES
    def __init__(self,EntityList,board,DispalyString:str="",XPosition:int=0,YPosition:int=0,deltaX:int=0,deltaY:int=0,iD:str = "",destroyOthersCallback = None):
        self.DisplayText = DispalyString
        self.xPosition = XPosition
        self.yPosition = YPosition
        self.deltaX = deltaX
        self.deltaY = deltaY
        self.iD = iD
        self.entityList =EntityList
        self.collisionCallback = destroyOthersCallback
        self.render(board)

