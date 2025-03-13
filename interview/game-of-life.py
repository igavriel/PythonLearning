# https://playgameoflife.com/

import select
from typing import List

class Cell:
    debug = False
    def __init__(self, x : int, y: int, live : bool) :
        self.x = x
        self.y = y
        self.live = live 

    def __str__(self):
        s = "*" if self.live is True else "-"
        if Cell.debug is True:
            return f"[{self.x},{self.y}]={s}"
        else:
            return f"{s}"

class LifeCell:
    def __init__(self, cell : Cell):
        x = cell.x
        y = cell.y
        row1 = [Cell(x-1, y-1,False), Cell(x-1,y,False),    Cell(x-1,y+1,False)]
        row2 = [Cell(x, y-1,False),   cell,                 Cell(x,y+1,False)]
        row3 = [Cell(x+1, y-1,False), Cell(x+1,y,False),    Cell(x+1,y+1,False)]
        self.nbr = [row1, row2, row3]
        self.countLive = 0
        self.countDead = 8

    def __str__(self):
        grid = ""
        for i in range(3):
            grid += f"{self.nbr[i][0]} {self.nbr[i][1]} {self.nbr[i][2]}\n"
        return grid

    def getCenter(self) -> Cell:
        return self.nbr[1][1]

    def getTopLeft(self) -> Cell:
        return self.nbr[0][0]

    def getBottomRight(self) -> Cell:
        return self.nbr[2][2]

    def areNbr(self, other: Cell) -> bool:
        xdif =  abs(other.x - self.getCenter().x)
        ydif =  abs(other.y - self.getCenter().y)
        if xdif <= 1 and ydif <=1:
            return True
        return False

    def add(self, other: Cell):
        if self.areNbr(other) is True:
            posX = other.x - self.getCenter().x + 1
            posY = other.y - self.getCenter().y + 1
            # check live changes
            if other.live != self.nbr[posX][posY].live:
                if other.live is True:
                    self.countDead -=1
                    self.countLive +=1
                else:
                    self.countDead +=1
                    self.countLive -=1
            
            self.nbr[posX][posY]=other

    '''
    # Rule 1 - Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    # Rule 2 - Any live cell with two or three live neighbours lives on to the next generation.
    # Rule 3 - Any live cell with more than three live neighbours dies, as if by overpopulation.
    # Rule 4 - Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    '''
    def PlayRound(self):
        # Rule 1
        if self.countLive < 2:
            self.getCenter().live = False
        # Rule 2
        if self.countLive == 2 or self.countLive == 3:
            self.getCenter().live = True
        # Rule 3
        if self.countLive > 3:
            self.getCenter().live = True

        # Rule 4 - count dead nbrs
        # 0,0   0,1   0,2
        # 1,0   1,1   1,2
        # 2,0   2,1   2,2
        # build temp grid 5x5
        row0 = [Cell(0, 0,False), Cell(0,1,False), Cell(0,2,False), Cell(0,3,False), Cell(0,4,False)]
        row1 = [Cell(1, 0,False), self.nbr[0][0], self.nbr[0][1], self.nbr[0][2], Cell(1,4,False)]
        row2 = [Cell(2, 0,False), self.nbr[1][0], self.nbr[1][1], self.nbr[1][2], Cell(2,4,False)]
        row3 = [Cell(3, 0,False), self.nbr[2][0], self.nbr[2][1], self.nbr[2][2], Cell(3,4,False)]
        row4 = [Cell(4, 0,False), Cell(4,1,False), Cell(4,2,False), Cell(4,3,False), Cell(4,4,False)]
        rule4 = [row0, row1, row2, row3, row4]

        # iterate inner matrix 1,1 -> 3,3
        i, j = 1, 1
        while i < 4 and j < 4:
            if rule4[i][j].live is False:
                count = 0
                for iterX in range(i-1, i+1):
                    for iterY in range(j-1, j+1):
                        if iterX != i and iterY != j:
                            if rule4[iterX][iterY].live is True:
                                count += 1
                if count == 3:
                    self.nbr[i-1][j-1].live = True

            i += 1
            j += 1

class Grid():
    def __init__(self, cells : List[Cell]):
        assert(len(cells)>0)
        
        # add list of cell to grid set
        self.board = set()
        for curCell in cells:
            self.board.add(LifeCell(curCell))
        
        # iterate all board and match nbr (double loop)
        for curLifeCell in self.board:
            for curCell in cells:
                are_nbr = curLifeCell.areNbr(curCell)
                if are_nbr is True:
                    curLifeCell.add(curCell)

    '''
    Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    Any live cell with two or three live neighbours lives on to the next generation.
    Any live cell with more than three live neighbours dies, as if by overpopulation.
    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    '''
    def PlayRound(self):
        for c in self.board:
            c.PlayRound()

    def __str__(self):
        cells = ""
        for c in self.board:
            cells += f"{c}\n"
        return cells


listCells = [
    Cell(1,1,True),
    Cell(1,0,True),
    Cell(0,1,True),

    #Cell(3,1,True),
    
    # Cell(6,1, True),
    # Cell(6,2, True),
    
    # Cell(9,1, True),
    # Cell(9,2, True),
    # Cell(9,3, True),

    # Cell(12,1, True),
    # Cell(12,2, True),
    # Cell(12,3, True),
    # Cell(13,1, True),
]

# n1 = CellWithNbr(c1)
# n1.add(c2)
# n1.add(c3)
# n1.add(c4)
# print (n1)

g = Grid(listCells)
print(g)
print("Round")
g.PlayRound()
print(g)