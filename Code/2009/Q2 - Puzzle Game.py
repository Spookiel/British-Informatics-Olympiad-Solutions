
from copy import deepcopy
class Board:
    def __init__(self,raw):
        self.raw = raw
        self.gridStore = [[j for j in i] for i in raw.splitlines()]
        self.gridCopy = [[[], 0] for item in deepcopy(self.gridStore)]
        self.total = 0
        for i in range(4):
            for j in range(4):
                self.gridCopy[j][0].append(self.gridStore[i][j])

        for ind in range(4):
            self.gridCopy[ind][0] = self.gridCopy[ind][0][::-1]
    def playTurn(self):


        # remove all adjacent blocks of colour NO DIAGS and count them
        # move old blocks down
        # add new blocks in
        toScore = self.removeAdj()
        #print(toScore)
        self.shuffleDown()
        self.addNew()

        if not toScore:
            return False

        cur = 1
        for i in toScore:
            cur *= len(i)
        self.total += cur
        return True



    def removeAdj(self):
        scoords = set()
        for i in range(4):
            for j in range(4):
                scoords.add((j, i))
        groups = set()
        while scoords:
            ne = scoords.pop()
            group = set()
            group.add(ne)
            col = self.gridStore[ne[1]][ne[0]]
            queue = [ne]
            while queue:
                x, y = queue.pop(0)
                for dx, dy in [[0,1], [1,0], [-1,0], [0,-1]]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < 4 and 0 <= ny < 4:
                        if self.gridStore[ny][nx]==col and (nx, ny) in scoords:
                            queue.append((nx, ny))
                            scoords.remove((nx, ny))
                            group.add((nx,ny))
            if len(group) > 1:
                #print(group)
                for cx, cy in group:
                    self.gridStore[cy][cx]="."
                groups.add(tuple(group))


        return groups

    def shuffleDown(self):
        #print(self.gridCopy)
        for k in range(4):
            for i in range(3):
                for j in range(4):
                    if self.gridStore[i+1][j]==".":
                        self.gridStore[i+1][j] = str(self.gridStore[i][j])
                        self.gridStore[i][j] = "."

    def addNew(self):
        #print(self.gridCopy)


        for i in range(4):
            for j in range(3,-1,-1):
                if self.gridStore[j][i]==".":
                    self.gridStore[j][i] = str(self.gridCopy[i][0][self.gridCopy[i][1]])
                    self.gridCopy[i][1] += 1
                    self.gridCopy[i][1] %= 4











raw = "\n".join([input().strip() for i in range(4)])
Solver = Board(raw)
flag = True
while flag:
    n = int(input())
    if n==0:
        break




    for turn in range(n):
        a = Solver.playTurn()
        if not a:
            print("GAME OVER")
            flag = False
            break
    if flag:
        for row in Solver.gridStore:
            print("".join(row))
        print()
    print(Solver.total)
