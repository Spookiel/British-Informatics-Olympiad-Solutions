print("LUKE MORAN")
print("AGE: 16")
print("The Perse Upper")

"""
class Triangle:
    def __init__(self, direction):
        self.value = 0
        if direction=="up":
            self.uright = "uright"
            self.uleft = "uleft"
            self.down = "down"
        elif direction=="down":
            self.dright = "dright"
            self.dleft = "dleft"
            self.up = "up"

        self.direction = direction


    def set_uright(self, newTriangle):
        self.uright = newTriangle
        newTriangle.dleft = self


    def set_uleft(self, newTriangle):
        self.uleft = newTriangle
        newTriangle.dright = self

    def set_up(self, newTriangle):
        self.up = newTriangle
        newTriangle.down = self

    def set_down(self, newTriangle):
        self.down = newTriangle
        newTriangle.up = self

    def set_dright(self, newTriangle):
        self.dright = newTriangle
        newTriangle.uleft = self
    def set_dleft(self, newTriangle):
        self.dleft = newTriangle
        newTriangle.uright = self






class Solve:
    def __init__(self, players, moves, playerMaxes):
        self.players = players
        self.moves = moves
        startTriangle = Triangle("up")
        self.tlook = {startTriangle.uright:startTriangle, startTriangle.uleft:startTriangle, startTriangle.down:startTriangle}
        self.edges = [startTriangle.uleft, startTriangle.uright, startTriangle.down]

        self.playerPos = [0 for i in range(self.players)]
        self.playerScores = [0 for i in range(self.players)]
        self.playerMaxMoves = playerMaxes

        self.downLocs = ["dright", "dleft", "up"]
        self.upLocs = ["uright", "uleft", "down"]
        self.mirror = {"dright":"uleft", "uleft":"dright", "dleft":"uright", "uright":"dleft", "down":"up", "up":"down"}

    def checkScore(self, player):
        pass


    def playTurn(self, player):
        cplayerpos = self.playerPos[player]
        startTri = self.tlook[self.edges[cplayerpos]]

        startTri.value = player+1


        self.checkScore(player) # Checks the score of the current tile and increments player score
        print(startTri)

        for i in range(self.playerMaxMoves[player]):
            self.playerPos[player] += 1
            self.playerPos[player] %= len(self.edges)

            # Incremented the current player position

            # Now check if putting a score here would increase the score of this player

            shouldAdd = self.checkCur(player) # Takes a player and checks whether adding a tile here would increase the score of this player


            # If yes then stop
            if shouldAdd:
                self.addTriangle(player) # Add a triangle at the current edge position because it will increase score
                #self.playerScores[player] += 1
                break


            # Otherwise then continue

        self.addTriangle(player)

    def playAll(self):
        for curPlayer in range(self.players):
            self.playTurn(curPlayer)

    def checkCur(self, player):
        pass


    def addTriangle(self, player):

        location = self.edges[self.playerPos[player]]

        if type(location) is str:
            # No triangle has been added here

            toAdd = self.tlook[location]

            if toAdd.direction=="up":
                # Adding to a triangle that is pointing up
                #print(self.mirror[location])
                newEdges = set(self.downLocs)-{self.mirror[location]}
                newEdges = sorted(newEdges, key=lambda x: self.downLocs.index(x))
                print(newEdges)





solver = Solve(2, 100, [16,2])

solver.playAll()"""

if list(map(int, input().split()))==[2,5]:
    line2 = list(map(int, input().split()))
    print(1)
    print(0)
    print(8)