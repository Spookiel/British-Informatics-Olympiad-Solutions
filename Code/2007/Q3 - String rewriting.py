import time

from collections import deque,Counter,defaultdict


s = list(input())
steps, p = list(map(int, input().split()))
start = time.time()

def total(d):
    return sum([i for i in d.values()])

def merge(a,b):
    for i in b:
        a[i] += b[i]
    return a

from functools import lru_cache

def solve(letter, steps):
    if steps==0:
        di = defaultdict(int)
        di[letter] = 1
        return di
    if letter=="A":
        return solve("B", steps-1)
    elif letter=="B":
        return merge(solve("A", steps-1),solve("B", steps-1))
    elif letter=="C":
        di = defaultdict(int)
        di["C"] = 2**(steps-1)
        di["D"] = 2**(steps-1)
        return di
    elif letter=="D":
        di = defaultdict(int)
        di["D"] = 2**(steps-1)
        di["C"] = 2**(steps-1)
        return di
    else:
        di = defaultdict(int)
        di["E"] = 2**steps
        return di


lookup = {"A":"B", "B":"AB", "C":"CD", "D":"DC", "E":"EE"}
import time
startTime = time.time()

doing = deque()

for i in s:
    doing.insert(0, (i, 0))
ans = defaultdict(int)
while doing and p:


    ne,depth = doing.pop()
    score = solve(ne, steps-depth)
    #print(ne, depth, score)
    if total(score) <= p:
        #print("ADDING", score, ne, depth)
        p -= total(score)
        ans = merge(ans, score)
    else:
        #print("CAN'T ADD", ne, depth, score)
        flag = False
        for i in lookup[ne][::-1]:
            if depth+1 <= steps:
                doing.append((i, depth+1))
            else:
                break
#print(ans)
for i in "ABCDE":
    print(ans[i], end=" ")


print("\n")
print(time.time()-startTime)