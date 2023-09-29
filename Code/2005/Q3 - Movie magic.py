

from functools import lru_cache


@lru_cache(maxsize=None)
def solve(state):


    finished = True
    stateCheck = list(state)
    pairs = [stateCheck[i:i+2] for i in range(0, len(stateCheck), 2)]


    for actor in pairs:
        if actor[0] > actor[1]:
            return 0
        elif actor[0] < actor[1]:
            finished = False
    if finished:
        return 1

    total = 0
    for actorInd, actor in enumerate(pairs):
        canChange = True
        for seniorActor in pairs[:actorInd]:
            if seniorActor[0] <= actor[0]:
                canChange = False
        if canChange:
            copState = list(stateCheck)
            copState[actorInd*2] += 1
            total += solve(tuple(copState))
    return total


actors  = int(input())
start = []
inp = list(map(int, input().split()))
for i in inp:
    start.append(0)
    start.append(i)
print(solve(tuple(start)))