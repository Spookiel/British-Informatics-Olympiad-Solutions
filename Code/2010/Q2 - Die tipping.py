

from collections import defaultdict



class Die:


    HEADINGS = {0: (0, -1), 90:(1, 0), 180:(0,1), 270:(-1,0)}

    def __init__(self):



        self.top = 1
        self.up = 2
        self.left = 3

        self.heading = 0


    def tip(self):

        if self.heading == 0:
            ### Tips towards top of board, so
            upcop = int(self.up)
            self.up = self.top
            self.top = 7-upcop



        elif self.heading == 90:
            ###Right turn
            topcop = int(self.top)
            self.top = self.left
            self.left = 7-topcop




        elif self.heading == 180:

            topcop = int(self.top)
            self.top = self.up
            self.up = 7-topcop


        elif self.heading == 270:
            leftcop = int(self.left)
            self.left = self.top
            self.top = 7-leftcop

    def __repr__(self):
        return f"Top: {self.top}, Up: {self.up}, Left:{self.left}"



    def move(self, grid_val):

        ret = grid_val+self.top
        if ret > 6:
            ret -= 6

        if ret == 1 or ret == 6:
            ### Need to return new position too
            ### Move one space according to the heading
            pass

        if ret == 2:
            self.heading += 90
            self.heading %= 360
        if ret == 3 or ret == 4:
            self.heading += 180
            self.heading %= 360
        if ret == 5:
            self.heading -= 90
            self.heading %= 360

        return tuple([ret]+[i for i in Die.HEADINGS[self.heading]])


class Grid:

    grid = defaultdict(lambda: 1)
    def __init__(self, initgrid):

        self.diex = 0
        self.diey = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                self.grid[(j,i)] = initgrid[i+1][j+1]


    def show_grid(self):

        for gy in range(self.diey-1, self.diey+2):
            for gx in range(self.diex-1, self.diex+2):
                if gx < -5 or gy < -5 or gy > 5 or gx > 5:
                    print("x", end="")
                else:
                    print(self.grid[(gx, gy)], end="")
            print()




    def move_die(self, die):

        self.diex += 5
        self.diex %= 11
        self.diex -= 5

        self.diey += 5
        self.diey %= 11
        self.diey -= 5



        nval, dx,dy = die.move(self.grid[(self.diex,self.diey)])


        self.grid[(self.diex, self.diey)] = nval
        self.diex += dx
        self.diey += dy





testdie = Die()

lines = [list(map(int, input().split())) for i in range(3)]

realgrid =  Grid(lines)

while 1:
    turns = int(input())
    if not turns:
        break


    for x in range(turns):
        realgrid.move_die(testdie)
        testdie.tip()

    realgrid.show_grid()


