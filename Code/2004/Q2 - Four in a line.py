

class Board:


    BOARD = [[-1 for col in range(7)]  for row in range(6)]
    cheight = [0 for i in range(7)] ###Keeps track of the height of each column
    def __init__(self):
        self.player = 0
        self.finished = False



    def play(self, col: int, player, test=False):

        flag = False
        if self.cheight[col] < 6:


            self.BOARD[self.cheight[col]][col] = player
            self.cheight[col] += 1
            flag = True

        if not test:
            self.player = 1-player
        return flag


    ### Play every possible move for the current player and check if any of them win
    ###


    def check_cols(self, player):

        for col in range(7):
            for fpos in range(3):
                ### Get next four
                res = [self.BOARD[fpos+i][col] == player for i in range(4)]

                if all(res):

                    return True
        return False

    def check_rows(self, player):

        for col in range(6):
            for fpos in range(4):
                ### Get next four
                res = [self.BOARD[col][fpos+i] == player for i in range(4)]
                if all(res):
                    return True
        return False

    def check_diags(self, player):
        ## Only need to go up, right, and up and left


        for row in range(6):
            for col in range(7):
                cy = row
                cx = col
                c = 0

                while self.BOARD[cy][cx] == player:
                    #print(self.BOARD[cy][cx], player, self.BOARD[cy][cx] == player, cx, cy)
                    c += 1
                    ### Check going up and left first
                    cy += 1
                    cx -= 1
                    if not 0 <= cx < 7 or not 0 <= cy < 6:
                        break




                if c==4:
                    return True

                cy = row
                c = 0
                cx = col


                while self.BOARD[cy][cx] == player:
                    #print(self.BOARD[cy][cx], player, self.BOARD[cy][cx] == player, cx, cy)
                    c += 1
                    ### Check going up and left first
                    cy += 1
                    cx += 1
                    if not 0 <= cx < 7 or not 0 <= cy < 6:
                        break

                if c==4:
                    return True

                #print(f"ROW {row} COL {col} COUNT {c}")

        return False

    def check_win(self, player):
        ### Checks if the current player wins the game
        ### Trying to find 4 in a row anywhere

        ### Check columns first

        return self.check_cols(player) or self.check_diags(player) or self.check_rows(player)


    def not_full(self, col):
        return self.BOARD[-1][col] == -1
    def choose_next(self):

        if self.finished:
            return -1

        #print(self.cheight, "BEFORE")

        ### Rule One

        bmove = -1
        for poscol in range(7):
            played = self.play(poscol, self.player, True)

            if self.check_win(self.player):
                bmove = poscol
                if played: self.undo_move(poscol)
                break


            if played:
                self.undo_move(poscol)

        if bmove != -1:
            #print("RULE ONE")
            return bmove


        ### Rule Two

        for poscol in range(7):
            played = self.play(poscol, 1-self.player, True)
            if self.check_win(1-self.player):
                bmove = poscol
                if played: self.undo_move(poscol)
                break
            if played:
                self.undo_move(poscol)

        if bmove != -1:
            #print("RULE TWO")
            return bmove

        ### Rule 3


       # print(self)
        #print(self.BOARD)
        #print(self.cheight)

        bmove =-1
        for ccol in range(7):
            if self.cheight[ccol] < 7 and self.not_full(ccol):
                bmove = ccol
                break

        if bmove != -1:
            #print("RULE THREE", ccol, self.cheight[ccol], "PLAYING INTO", self.BOARD[self.cheight[ccol]][ccol])
            return bmove
        return -1




    def play_next(self):

        if self.finished:
            return
        nmove = self.choose_next()

        if nmove == -1:
            #print("NO VALID MOVE FOUND FOR PLAYER")
            return
        else:
            #print("VALID MOVE FOUND FOR PLAYER", self.player, nmove, self.cheight)
            pass

        self.play(nmove, self.player)


        #print(self)
        #print("PLAY_NEXT", self.finished, self.check_win(self.player), self.check_win(1-self.player))

        if self.check_win(1-self.player):
            print(f"PLAYER {1-self.player+1} WINS!")
            self.finished = True







    def undo_move(self, col):

        self.cheight[col] -= 1

        self.BOARD[self.cheight[col]][col] = -1


    def __repr__(self):

        s = ""
        for row in self.BOARD[::-1]:
            for item in row:
                if item == -1:
                    s += "-"
                elif item == 0:
                    s += "*"
                else:
                    s += "o"
            s += "\n"
        return s

"""
TESTBOARD = Board()
for i in range(4):
    TESTBOARD.BOARD[i][i] = 0


assert TESTBOARD.check_diags(0)"""



n = int(input())

b = Board()
moves = list(map(int, input().split()))

for m in moves:
    b.play(m-1, b.player)


while 1:
    x = input()
    if x == "n":
        b.play_next()

        print(b)
    elif x == "r":

        while not b.finished:
            b.play_next()

            print(b)
        break





