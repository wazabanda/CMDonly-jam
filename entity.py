class entity():
    DisplayText = ""
    xPosition = 0
    yPosition = 0
    deltaX = 0
    deltaY = 0
    def __init__(self,DispalyString,XPosition,YPosition,deltaX=0,deltaY=0):
        self.DisplayText = DispalyString
        self.XPosition = XPosition
        self.YPosition = YPosition
        self.deltaX = deltaX
        self.deltaY = deltaY
    def move(self,x,y,board):
        if x + y != 0:
            board[self.yPosition][self.xPosition] = "* "
            if self.xPosition + x < len(board[0]) and self.xPosition + x >= 0:
                self.xPosition += x
            if self.yPosition + y < len(board) and self.yPosition + y >= 0:
                self.yPosition += y
        
    def render(self,board):
        board[self.yPosition][self.xPosition] = self.DisplayText
        
    def update(self,board):
        ##self.render(board)
        self.move(self.deltaX, self.deltaY, board)