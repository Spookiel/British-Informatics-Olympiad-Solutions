
from collections import defaultdict

class Board:
    def __init__(self, dis, instructions, m):
        self.grid = defaultdict(int)
        self.dis = dis
        self.instructions = instructions
        self.moves = m
        self.pos = (0,0)
        self.dir = 90 #0 is up, 90 is right


    def pboard(self):
        for i in range(-5, 5):
            for j in range(-5, 5):
                print(self.grid[(j, i)], end= " ")
            print("\n")
        print("-"*50)
        print(f"Explorer location {self.pos[0]} {self.pos[1]}")
        print("-" * 50)
dis, instructions, moves = input().split()

dis = int(dis)
moves = int(dis)

solve = Board(dis, instructions, moves)

solve.pboard()


