


#store the windows as a set and then compute transformations as a graph
from itertools import permutations
from collections import defaultdict,deque
distances = defaultdict(lambda:999999)

def add(cur, other):
    cur += other[0]
    other = other[1:]
    return cur, other


def swap(cur, other):
    cur = list(cur)
    cur[0], cur[1] = cur[1], cur[0]
    return "".join(cur), other




def rotate(cur, other):
    first = cur[0]
    cur = cur[1:]
    cur += first
    return cur,other




alpha = "ABCDEFGH"


import time

start = time.time()


def solve(target):
    queue = deque()
    queue.append(["", alpha[:len(target)], 0])


    while queue:
        cur, other, distance = queue.popleft()
        distances[cur] = distance

        if len(other) > 0:
            newState, newOther = add(cur, other)

            if distance+1 < distances[newState]:
                distances[newState] = distance+1
                queue.append((newState, newOther, distance+1))
        if len(cur) > 1:
            newState, newOther = swap(cur, other)

            if distance+1 < distances[newState]:
                distances[newState] = distance+1
                queue.append((newState, newOther, distance+1))

            newState, newOther = rotate(cur, other)
            if distance+1 < distances[newState]:
                distances[newState] = distance+1
                queue.append((newState, newOther, distance+1))


    return distances[target]

for perm in permutations("ABCDE"):
    if solve("".join(perm))==6:
        print("".join(perm), solve("".join(perm)))