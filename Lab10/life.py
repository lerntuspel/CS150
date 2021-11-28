#life.py
#Game of Life
import drawing

#Assuming the perameters HEIGHT and WIDTH and CELL_SIZE exist within the program that calls on these classes
class Cell():
    def __init__(self, x, y, alive=False):
        self.x = x
        self.y = y
        self.last = alive
        self.alive = alive
    #suppose celss = [cell[1][1], ... cell[maxx][maxy]]
    def countNeighbors(self, cells):
        xCoords = []
        yCoords = []
        liveCount = 0
        #tries to figure out which cells to count over

        #top boarder
        if (self.x==0):
            xCoords = [len(cells)-1,0,1]
        #bottom boarder
        elif (self.x==(len(cells)-1)):
            xCoords = [self.x-1,self.x,0]
        #everything else
        else:
            xCoords = [self.x-1,self.x,self.x+1]
        #Left boarder
        if (self.y==0):
            yCoords = [len(cells[self.x])-1,0,1]
        #Right boarder
        elif (self.y==(len(cells[self.x])-1)):
            yCoords = [self.y-1,self.y,0]
        #everything else
        else:
            yCoords = [self.y-1,self.y,self.y+1]

        #Count live cells in the 9x9
        for x in xCoords:
            for y in yCoords:
                if cells[x][y].last==True:
                    liveCount= liveCount + 1
        #Because the loops before included the cell we are checking the neighbors of
        #We need to reduce the count by 1 if self was alive
        if self.last==True:
            liveCount = liveCount - 1
        return liveCount

    def update(self, cells):
        #rules of the game of life
        liveNeighbors = self.countNeighbors(cells)
        if ((liveNeighbors<=1)or(liveNeighbors>=4)):
            self.alive = False
        elif (liveNeighbors==2):
            self.alive = self.last
        elif (liveNeighbors==3):
            self.alive = True

class Board():
    def __init__(self, width, height):
        self.cells = []
        self.width = width
        self.height = height
        for i in range(self.width):
            #create new column
            self.cells.append([])
            for j in range(self.height):
                #cell in column
                self.cells[i].append(Cell(i, j, False))
    def initialize(self, setup):
        if setup == 1:
            # create one hotspot
            self.cells[24][25].alive = 1
            self.cells[24][26].alive = 1
            self.cells[25][24].alive = 1
            self.cells[25][25].alive = 1
            self.cells[26][25].alive = 1

        if setup == 2:
            self.cells[3][15].alive = 1
            self.cells[3][16].alive = 1
            self.cells[4][15].alive = 1
            self.cells[4][16].alive = 1

            self.cells[23][15].alive = 1
            self.cells[23][16].alive = 1
            self.cells[24][15].alive = 1
            self.cells[24][16].alive = 1

            self.cells[10][13].alive = 1
            self.cells[9][14].alive = 1
            self.cells[8][15].alive = 1
            self.cells[9][16].alive = 1
            self.cells[10][17].alive = 1

            self.cells[12][12].alive = 1
            self.cells[12][13].alive = 1
            self.cells[11][14].alive = 1
            self.cells[11][15].alive = 1
            self.cells[11][16].alive = 1
            self.cells[12][17].alive = 1
            self.cells[12][18].alive = 1

            #test with a known setup and expected outcome
        if setup == 3:
            self.cells[8][7].alive = 1
            self.cells[9][8].alive = 1
            self.cells[7][9].alive = 1
            self.cells[8][9].alive = 1
            self.cells[9][9].alive = 1

    def update(self):
        #store previous information first
        for i in range(self.width):
            for j in range(self.height):
                self.cells[i][j].last = self.cells[i][j].alive
        #then update
        for i in range(self.width):
            for j in range(self.height):
                self.cells[i][j].update(self.cells)

    def draw(self, canvas, force=False):
        canvas.setOutlineColor(0,0,0)
        canvas.setFillColor(250,250,250)
        #Either draw all or draw the ones that changed
        if (force==True):
            for i in range(self.width):
                for j in range(self.height):
                    if self.cells[i][j].alive:
                        canvas.setFillColor(200,0,0)
                        canvas.drawRectFill(i*CELL_SIZE, j*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    else:
                        canvas.setFillColor(250,250,250)
                        canvas.drawRectFill(i*CELL_SIZE, j*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        #Draw only the cells that are no the same state as their previous interation
        else:
            for i in range(self.width):
                for j in range(self.height):
                    if self.cells[i][j].alive != self.cells[i][j].last:
                        if self.cells[i][j].alive:
                            canvas.setFillColor(200,0,0)
                            canvas.drawRectFill(i*CELL_SIZE, j*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        else:
                            canvas.setFillColor(250,250,250)
                            canvas.drawRectFill(i*CELL_SIZE, j*CELL_SIZE, CELL_SIZE, CELL_SIZE)
