
from collections import defaultdict

class Board:
    def __init__(self, dis, instructions, m):
        self.grid = defaultdict(int)
        self.dis = dis
        self.instructions = instructions
        self.movePos = 0
        self.moves = m
        self.pos = (0,0)
        self.dir = 0 #0 is up, 90 is right
        self.instLookup = {"L":-90, "R":90, "F":0}
        self.dirLookup = {0:(0,-1), 90:(1,0), 180:(0,1),270:(-1,0), 360:(0,-1)}

        #print("GOT", self.moves, self.dis, self.instructions)

    def pboard(self):
        for i in range(-3, 3):
            for j in range(-3, 3):
                print(self.grid[(j, i)], end= " ")
            print("\n")
        print("-"*50)
        print(f"Explorer location {self.pos[0]} {self.pos[1]}")
        print("-" * 50)


    def move(self):
        self.grid[self.pos] = self.dis+1

        nextMove = self.instructions[self.movePos]
        self.movePos += 1
        self.movePos %= len(self.instructions)

        self.dir += self.instLookup[nextMove]
        self.dir %= 360

        canMove = False

        for done in range(4):
            newPos = (self.pos[0]+self.dirLookup[self.dir][0], self.pos[1]+self.dirLookup[self.dir][1])

            if self.grid[newPos]==0:
                self.pos = newPos
                canMove = True
                break

            self.dir += 90
            self.dir %= 360


        return canMove

    def updateGrid(self):

        for i in self.grid.keys():
            if self.grid[i] > 0:
                self.grid[i] -= 1
    def main(self):
        #self.moves += 1
        #print(self.moves, "MOVING")
        while self.moves:

            self.updateGrid()
            #self.pboard()
            canMove = self.move()

            if not canMove:
                return False

            self.moves -= 1
        return True
dis, instructions, moves = input().split()

dis = int(dis)
moves = int(moves)

solve = Board(dis, instructions, moves)

finished = solve.main()
#print(finished)
ans = list(solve.pos)

ans[1] *= -1

print(f"({ans[0]},{ans[1]})")


