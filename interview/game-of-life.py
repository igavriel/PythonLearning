from typing import List
import math

class Cell:
    
    def __init__(self, x : int, y: int, live : bool) :
        self.x = x
        self.y = y
        self.live = live 

    def __str__(self):
        s = "*" if self.live is True else "-"
        return f"[{self.x},{self.y}]={s}"


class CellWithNbr:
    def __init__(self, cell : Cell):
        x= cell.x
        y= cell.y
        row1 = [Cell(x-1, y-1,False), Cell(x-1,y,False),    Cell(x-1,y+1,False)]
        row2 = [Cell(x, y-1,False),   Cell(x,y, cell.live), Cell(x,y+1,False)]
        row3 = [Cell(x+1, y-1,False), Cell(x+1,y,False),    Cell(x+1,y+1,False)]
        self.nbr = [row1, row2, row3]

    def __str__(self):
        grid = ""
        for i in range(3):
            grid += f"{self.nbr[i][0]} {self.nbr[i][1]} {self.nbr[i][2]}\n"
        return grid

    def getCenter(self) -> Cell:
        return self.nbr[1][1]

    def areNbr(self, other: Cell) -> bool:
        xdif =  abs(other.x - self.getCenter().x)
        ydif =  abs(other.y - self.getCenter().y)
        if xdif <= 1 and ydif <=1:
            return True
        return False

    def add(self, other: Cell):
        if self.areNbr(other) is True:        
            self.nbr[other.x-self.getCenter().x +1][other.y-self.getCenter().y +1]=other


class Grid():
    def __init__(self, cells : List[Cell]):
        assert(len(cells)>0)
        
        self.board = set()
        for curCell in cells:
            self.board.add(CellWithNbr(curCell))
        
        for curNbrCell in self.board:
            for curCell in cells:
                are_nbr = curNbrCell.areNbr(curCell)
                if are_nbr is True:
                    curNbrCell.add(curCell)
            
        
        # for index in range(1, len(cells)):
        #     curCell = cells[index]
        #     for curLive in self.board:
        #         are_nbr = curLive.areNbr(curCell)
        #         newCell = CellWithNbr(curCell)
        #         self.board.add(newCell)
        #         if are_nbr is True:
        #             curLive.add(curCell)
        #             newCell.add(curLive.getCenter())

    def __str__(self):
        cells = ""
        for c in self.board:
            cells += f"{c}\n"
        return cells


listCells = [Cell(1,1,True),
Cell(1,0,True),
Cell(0,1,True),
Cell(3,1,True)
]

# n1 = CellWithNbr(c1)
# n1.add(c2)
# n1.add(c3)
# n1.add(c4)
# print (n1)

g = Grid(listCells)
print(g)