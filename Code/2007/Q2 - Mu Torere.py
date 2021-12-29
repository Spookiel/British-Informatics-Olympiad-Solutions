

class Board:
    PLAYERLOOK = {"O":"X", "X":"O"}
    def __init__(self, state):
        self.center = state[0]
        self.nodes = list(state[1:])
        self.curPlayer = "O"


    def strategyOne(self):
        nextMoves = self.getNextMoves(self.center, self.nodes, self.curPlayer)
        nextPlayer = Board.PLAYERLOOK[self.curPlayer]
        for move in nextMoves:
            ccenter, cnodes = move
            if not self.getNextMoves(ccenter, cnodes, nextPlayer):
                print("FOUND MOVE")
                self.center = ccenter
                self.nodes = cnodes
                self.curPlayer = Board.PLAYERLOOK[self.curPlayer]
                return "Found"
        return "Failed"

    def strategyTwo(self):
        nextMoves = self.getNextMoves(self.center, self.nodes, self.curPlayer)
        nextPlayer = Board.PLAYERLOOK[self.curPlayer]
        first = None
        for move in nextMoves:
            ccenter, cnodes = move
            if first is None:
                first = ccenter, cnodes[:]
            for nextMovetwo in self.getNextMoves(ccenter, cnodes, nextPlayer):
                nccenter, ncnodes = nextMovetwo
                if self.getNextMoves(nccenter, ncnodes, self.curPlayer):
                    self.center = ccenter
                    self.nodes = cnodes
                    self.curPlayer = Board.PLAYERLOOK[self.curPlayer]
                    return "Found"
        if first is not None:
            self.center, self.nodes = first
            self.curPlayer = Board.PLAYERLOOK[self.curPlayer]
            return "Found"
        return "Failed"



    def strategyThree(self):
        nextMoves = self.getNextMoves(self.center, self.nodes, self.curPlayer)
        nextPlayer = Board.PLAYERLOOK[self.curPlayer]

        for move in nextMoves:
            self.center, self.nodes = move
            self.curPlayer = nextPlayer
            return "Found"

    def getNextMoves(self, center, nodes, curPlayer):
        # two possibilities, either center is empty or center is not empty

        if center=="E":
            #
            # center is empty
            # All my tiles can move into the center

            for ind, tile in enumerate(nodes):
                if tile == curPlayer and not (nodes[(ind-1)%8] == curPlayer and nodes[(ind+1)%8] == curPlayer):
                    cnodes = nodes[:]
                    cnodes[ind] = "E"
                    yield curPlayer, cnodes

        else:
            # There is a player in the center
            if center == curPlayer:
                for ind, tile in enumerate(nodes):
                    if tile=="E":
                        cnodes = nodes[:]
                        cnodes[ind] = curPlayer

                        yield "E", cnodes
                # Can move the center tile
            else:
                pass
                # can't move the center tile

    def playTurn(self):
        # Each strategy returns next board state
        if self.strategyOne()=="Found":
            return "Done"
        elif self.strategyTwo()=="Found":
            return "Done"
        elif self.strategyThree()=="Found":
            return "Done"
        return "No"


ansLook = ["", "O", "X"]
inp = input()

boardState = Board(inp)

for i in range(3):
    finished = boardState.playTurn()
    if finished=="No":
        print(boardState.center+"".join(boardState.nodes))
        print("Player", ansLook.index(Board.PLAYERLOOK[boardState.curPlayer]), "wins")
        break