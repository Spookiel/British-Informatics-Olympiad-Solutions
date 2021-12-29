import time

from collections import deque,defaultdict


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

@lru_cache(maxsize=None)
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib(n-1)+fib(n-2)


def solve(letter, steps):
    if steps==0:
        di = defaultdict(int)
        di[letter] = 1
        return di
    if letter=="A":
        di = defaultdict(int)
        di["A"] = fib(steps-1)
        di["B"] = fib(steps)
        return di
    elif letter=="B":
        di = defaultdict(int)
        di["B"] = fib(steps+1)
        di["A"] = fib(steps)
        return di
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


print("\n", end="")
print(f"FINISHED IN {time.time()-startTime}")