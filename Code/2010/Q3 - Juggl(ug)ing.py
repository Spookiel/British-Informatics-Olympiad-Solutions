
j ,n = list(map(int ,input().split()))
jugs = list(map(int, input().split()))

# SCORES 18/23

from copy import deepcopy
class Solver():
    def __init__(self ,jugs ,n):
        self.caps = jugs
        self.target = n
        self.numOfJugs = len(self.caps)
        self.jugs = [0] *self.numOfJugs
    def empty(self ,ind):
        self.jugs[ind] = 0
    def store(self):
        self.tempStore = deepcopy(self.jugs)

    def restore(self):
        self.jugs = deepcopy(self.tempStore)

    def fill(self ,ind):
        self.jugs[ind] = self.caps[ind]
    def transfer(self ,ind1 ,ind2):
        if self.jugs[ind1] >= self.caps[ind2]:
            self.jugs[ind1] = self.jugs[ind1 ] -(self.caps[ind2 ] -self.jugs[ind2])
            self.jugs[ind2] = self.caps[ind2]
        else:
            self.jugs[ind2] += self.jugs[ind1]
            self.jugs[ind2] = self.caps[ind2] if self.jugs[ind2] > self.caps[ind2] else self.jugs[ind2]
            self.jugs[ind1] -= self.jugs[ind2]
            if self.jugs[ind1] < 0:
                self.jugs[ind1] = 0

solve = Solver(jugs, n)
seen = set()
moves = [solve.fill, solve.empty]
seen.add(tuple(solve.jugs))
queue = []
queue.append((solve.jugs ,0))
from itertools import combinations
while queue:
    nextState ,distance = queue.pop(0)
    solve.jugs = nextState
    if n in solve.jugs:
        print(distance)
        break
    solve.store()
    # print("GOING FROM", nextState)
    for move in moves:
        for j in range(solve.numOfJugs):
            move(j)
            # print("CAN GET TO", solve.jugs)
            if tuple(solve.jugs) not in seen and tuple(solve.jugs) not in queue:

                queue.append((solve.jugs ,distance +1))
                seen.add(tuple(solve.jugs))
            solve.restore()
    for pair in combinations(range(solve.numOfJugs), 2):
        solve.transfer(pair[0], pair[1])
        if tuple(solve.jugs) not in seen and tuple(solve.jugs) not in queue:
            queue.append((solve.jugs ,distance +1))
            seen.add(tuple(solve.jugs))

        # print("CAN GET TO", solve.jugs)
        solve.restore()
        solve.transfer(pair[1] ,pair[0])

        if tuple(solve.jugs) not in seen and tuple(solve.jugs) not in queue:
            queue.append((solve.jugs ,distance +1))
            seen.add(tuple(solve.jugs))
        # print("CAN GET TO", solve.jugs)
        solve.restore()

    # print(queue)

