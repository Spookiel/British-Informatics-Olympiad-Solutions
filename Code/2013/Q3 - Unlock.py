
from collections import defaultdict
from copy import deepcopy
from string import ascii_letters
from itertools import combinations
alpha = ascii_letters
alphal = alpha[:len(alpha)//2]


class Board:

    def __init__(self, start):
        self.board = [[0 for i in range(5)] for j in range(5)]
        self.done = defaultdict(int)
        for i in start:
            ind = alpha.index(i)
            got = 1
            if ind >= 26:
                ind -=26
                got = 2

            if ind!=25:
                y,x = divmod(ind, 5)
                self.board[y][x] = got

    def pboard(self):
        for m in self.board:
            print(*m)
        print("-"*50)

    def convToCoords(self, letter):
        ind = alpha.index(letter)

        if ind >= 26:
            ind -= 26

        if ind != 25:
            y, x = divmod(ind, 5)
            #print(ind, letter, "HERE", "X", x, "Y", y)
            return (x, y)


    def toggle(self, letter, board,isSelf=True):
        if isSelf:
            x,y = self.convToCoords(letter)
            self.board[y][x] += 1
            self.board[y][x] %= 3


            for dx, dy in [[0,1], [1,0], [-1,0], [0,-1]]:
                try:
                    nx, ny = dx+x, y+dy
                    if nx >= 0 and ny >= 0:
                        self.board[ny][nx] += 1
                        self.board[ny][nx] %= 3

                except:
                    pass
        else:
            x, y = self.convToCoords(letter)
            board[y][x] += 1
            board[y][x] %= 3

            for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                try:
                    nx, ny = dx + x, y + dy
                    if nx >= 0 and ny >= 0:
                        board[ny][nx] += 1
                        board[ny][nx] %= 3

                except:
                    pass
            return board

    def reduce(self, board, dic,isSelf = True):

        if isSelf:
            for letter in alphal[5:-1]:
                x,y = self.convToCoords(letter)
                while self.board[y-1][x] != 0:
                    self.toggle(letter, [])
                    #self.pboard()
                    self.done[letter] += 1
        else:
            for letter in alphal[5:-1]:
                x,y = self.convToCoords(letter)
                #print(x,y, letter, self.board[y-1][x])
                while board[y-1][x] != 0:
                    #print("toggling", letter, self.convToCoords(letter), alphal.index(letter), "found invalid", y-1,x)
                    board = self.toggle(letter, board, isSelf = False)
                    #self.pboard()
                    dic[letter] += 1
                    dic[letter] %= 3
            return board,dic



    def fin(self):
        got = []
        for i in range(1, 6):
            for pos in combinations("abcde", i):
                done = deepcopy(self.done)
                cop = deepcopy(self.board)
                for let in pos:
                    cop = self.toggle(let, cop, isSelf=False)
                    done[let] += 1


                cop, newDone = self.reduce(cop, done, isSelf=False)

                if self.check(cop):
                    got.append(conv(done))
        return got



    def check(self, board):
        return sum([sum(i) for i in board])==0




def conv(dic):
    ans = ""
    for i in dic.keys():
        if dic[i]==2:
            ans += i.upper()
        elif dic[i]==1:
            ans += i
    return "".join(sorted(ans, key=lambda x: alphal.index(x.lower())))

solve = Board(input())


solve.reduce([],{}, isSelf=True)

if solve.check(solve.board):
    print(conv(solve.done))
answers = solve.fin()

if answers:
    print("\n".join(answers))
else:
    print("IMPOSSIBLE")

