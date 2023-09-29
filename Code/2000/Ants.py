class Ant:
    DIR_LOOK = {"T":0, "R":90, "L":270, "B":180}
    ANGLE_TO_LETTER = {j:i for (i,j) in list(DIR_LOOK.items())}
    ANGLE_TO_DELTA = {0: (0,1), 90:(1,0), 180:(0,-1), 270:(-1,0)}
    def __init__(self, x,y, dir):
        self.x = x
        self.y = y
        self.dir = Ant.DIR_LOOK[dir]

    @property
    def off_board(self):
        return 1 > self.x or 11 < self.x or 1 > self.y or 11 < self.y



    def step(self, grid):

        dx,dy = Ant.ANGLE_TO_DELTA[self.dir]
        nx, ny = self.x+dx, self.y+dy

        self.x = nx
        self.y = ny


        if not self.off_board:
            ### Get tile at the new position
            ntile = grid[(nx, ny)]

            if ntile.col == 0:
                ### Rotate right by 90
                self.dir += 90
                self.dir %= 360
            else:
                ### Rotate left by 90
                self.dir -= 90
                self.dir %= 360
            grid[(nx, ny)].col = 1-grid[(nx, ny)].col

    def __repr__(self):
        if self.off_board:
            return "Removed"
        else:
            return f"{self.x} {self.y} {Ant.ANGLE_TO_LETTER[self.dir]}"



class Tile:
    def __init__(self, x, y, col=0):
        ### 0 is a white tile and 1 is a black tile
        self.x = x
        self.y = y
        self.col = col

    def __repr__(self):
        return "." if not self.col else "*"

grid = {}
for i in range(1,12):
    for j in range(1,12):
        grid[(j,i)] = Tile(j, i)


def print_grid(grid):
    ### Prints the grid in the correct orientation

    for y in range(11,0,-1):
        for x in range(1,12):
            print(grid[(x,y)], end=" ")
        print()


x1,y1,d1 = input().split()
x2,y2,d2 = input().split()

x1,y1 = list(map(int, [x1,y1]))
x2,y2 = list(map(int, [x2,y2]))

a1 = Ant(x1,y1,d1)
a2 = Ant(x2,y2, d2)

while 1:
    n = int(input())
    if n == -1:
        break
    try:
        n1 = int(n)
    except:
        continue


    for turn in range(n):
        a1.step(grid)
        a2.step(grid)

    print_grid(grid)
    print(a1)
    print(a2)
