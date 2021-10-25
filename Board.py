class  BOARDclass():
    width = 0
    hight = 0
    defultPlaceHolder = ""
    grid = []
    def __init__(self,width=3,hight=3,defultPlaceHolder="* "):
        self.width = width
        self.height = hight
        self.defultPlaceHolder = defultPlaceHolder
        
        for i in range(hight):
            row = []
            for j in range(width):
                row.append(defultPlaceHolder)
            self.grid.append(row)