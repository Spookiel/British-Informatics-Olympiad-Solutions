

class Board:
    def __init__(self):

        self.p1Pos = "inp"
        self.p1Mod = "inp"

        self.p2Pos = "inp"
        self.p2Mod = "inp"


        self.vlines = [[None for i in range(5)] for i in range(5)]
        self.hlines = [[None for i in range(5)] for i in range(5)]

    def checkUp(self, cx, cy):
        nx, ny = cx, cy-1

        if 0 <= nx < 5 and 0 <= ny < 5:
            print("VALID COORDINATE FOR LINE")
            if self.vlines[ny][nx] is None:
                self.vlines[ny][nx] = 1
                return True
        return False

    def checkRight(self,cx,cy):
        nx,ny = cx,cy
        if 0 <= nx < 5 and 0 <= ny < 5:
            print("VALID COORDINATE FOR HORIZ LINE")
            if self.hlines[ny][nx] is None:
                self.hlines[ny][nx] = 1
                return True
        return False

    def checkDown(self, cx, cy):
        nx, ny = cx,cy
        if 0 <= nx < 5 and 0 <= ny < 5:
            if self.vlines[ny][nx] is None:
                self.vlines[ny][nx] = 1
                return True
        return False

    def checkLeft(self,cx,cy):
        nx, ny = cx-1,cy

        if 0 <= nx < 5 and 0 <= ny < 5:
            if self.hlines[ny][nx] is None:
                self.hlines[ny][nx] = 1
                return True
        return False


    def tryConnect(self, player):
        if player==1:
            cpx, cpy = self.dotToCoord(self.p1Pos)

            if self.checkUp(cpx, cpy):
                return True
            elif self.checkRight(cpx, cpy):
                return True
            elif self.checkDown(cpx, cpy):
                return True
            elif self.checkLeft(cpx, cpy):
                return True

            return False
            # go clockwise
        else:
            cpx, cpy = self.dotToCoord(self.p2Pos)
            if self.checkUp(cpx, cpy):
                return True
            elif self.checkLeft(cpx, cpy):
                return True
            elif self.checkDown(cpx, cpy):
                return True
            elif self.checkRight(cpx, cpy):
                return True

            return False
            # go counter clockwise for player 2


    def playOne(self):
        self.p1Pos += self.p1Mod
        self.p1Pos %= 37 # Because 1 through 36 inclusive
        while True:
            # Try to join a line to this square in clockwise order
            if self.tryConnect(1):
                # If success then break
                break

            self.p1Pos += 1
            self.p1Pos %= 37
        return True

    def playTwo(self):
        self.p2Pos += self.p2Mod
        self.p2Pos %= 37
        while True:
            if self.tryConnect(2): # Try to connect a line to the current tile that player two is at
                break

            self.p2Pos += 1
            self.p2Pos %= 37
        return True

    def dotToCoord(self, dot):
        return divmod(dot-1, 6)

    def countSquares(self, player):
        for box in range(25):
            cbx,cby = divmod(box, 5)
            if self.hlines[cbx]==1 and self.hlines[cbx]

    def playTurn(self):
        self.playOne()
        self.playTwo()

b = Board()

b.p1Pos = 4
b.p1Mod = 10
b.p2Pos = 14
b.p2Mod = 23

for i in range(23):
    b.playTurn()

for m in b.vlines:
    print(*m)

print("-")
for m in b.hlines:
    print(*m)

b.countSquares()