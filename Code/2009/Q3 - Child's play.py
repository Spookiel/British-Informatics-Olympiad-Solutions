
from functools import lru_cache
s,n = list(map(int, input().split()))



@lru_cache(maxsize=None)
def score(targ, cur=0):
    if cur > targ:
        return 0
    if cur==targ:
        return 1

    total = 0
    for i in range(1,min(targ-cur+1, 10)):
        total += score(targ,cur+i)
    return total


ans = []
while True:

    for i in range(1, s-sum(ans)+1):
        #print(i, score(s-(sum(ans)+i)), ans, n)
        if score(s-(sum(ans)+i)) >= n:
            ans.append(i)
            break
        else:
            n -= score(s-(sum(ans)+i))
    #print(ans, n)
    if sum(ans)==s:
        break
print(*ans)



def b():
    tot = 0
    for i in range(1,10):
        tot += 32//i
    print(tot)

# b() -> 88
"""
They are the same

"""