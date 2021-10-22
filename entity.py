class entity():
    DisplayText = ""
    xPosition = 0
    yPosition = 0
    def __init__(self,DispalyString,XPosition,YPosition):
        self.DisplayText = DispalyString
        self.XPosition = XPosition
        self.YPosition = YPosition
    def move(self,x,y,board):
        board[self.yPosition][self.xPosition] = "* "
        
        if self.xPosition + x < len(board[0]) and self.xPosition + x >= 0:
            self.xPosition += x
        if self.yPosition + y < len(board) and self.yPosition + y >= 0:
            self.yPosition += y
        board[self.yPosition][self.xPosition] = self.DisplayText