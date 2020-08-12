
from collections import Counter,deque


nums = ['ZERO','ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']

cdic = dict(zip(range(10), nums))


def conv(num):
    ans = ""
    for i in str(num):
        ans += cdic[int(i)]
    return ans

from functools import lru_cache

@lru_cache(maxsize=None)
def can(let1, let2):
    c = Counter(let1)
    c1 = Counter(let2)
    tdif = 0
    for let in c|c1:
        if c[let]!=c1[let]:
            tdif += abs(c[let]-c1[let])
    #print(tdif, let1, let2)
    return tdif <= 5


#print(can(conv(1), conv(90)))
#print(conv(1), conv(90))

lst = [conv(i+1) for i in range(999)]


def solve(s,f):
    switch = [[deque(), {}, 0], [deque(), {}, 0]]
    switch[0][0].append((s, 0))
    switch[1][0].append((f, 0))
    #print(switch)
    if can(conv(s), conv(f)):
        #print(1)
        return 1


    switch[0][1][s] = 0
    switch[1][1][f] = 0
    test = 1
    side = 0
    while True:
        while True:
            q, seen,cdist = switch[side]
            ne, dist = q.popleft()
            if dist != cdist:
                switch[side][-1] += 1
                break


            for i in range(1, 1000):
                if i-1!=ne-1 and can(lst[i-1], lst[ne-1]) and i not in seen:
                    seen[i] = dist+1

                    q.append((i, dist+1))


        #print(side, switch[side], "EHRE")

        a = set(switch[0][1].keys())&set(switch[1][1].keys())
        if a:
            #print(a, "COMMON")
            break
        #print(switch[0][1], switch[1][1])

        side = 1-side
        test += 1

    #print(test)
    #print("COMPLETED IN", time.time()-start)
    return test

import time

"""
for i in range(3):
    solve(*list(map(int, input().split())))
"""



def b():
    count = 0
    for i in range(1, 1000):
        if can(conv(i), "ZERO"):
            count += 1
    print(count, "FOR PART B")


#b) -> 15


def c():
    start = time.time()
    from itertools import combinations

    longest = 0
    count = 0
    for s,f in combinations(range(1, 1000), 2):
        flag = False
        for i in str(s):
            if i in str(f):
                flag = True
                break
        if flag:
            continue
        if s!=f:
            print(s,f)
            thing = solve(s, f)
            if thing > longest:
                longest = thing
                count = 0
            elif thing==longest:
                count += 1
    print("FOUND", count, "OF LENGTH", longest)
    print("COMPLETED IN", time.time()-start)




c()