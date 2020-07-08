from functools import lru_cache
from collections import defaultdict

s,d = list(map(int, input().split()))


@lru_cache(maxsize=None)
def solve(targ, left):
    if left==0:
        if targ==0:
            return 1
        return 0
    elif targ <= 0:
        return 0

    total = 0
    for i in range(1,21):
        total += solve(targ-i, left-1)
    return total


def run(s, d):
    ans = 0
    for i in range(1,21):
        ans += solve(s-(2*i), d-1)
    return ans

print(run(s, d))


def b():
    for score in range(4,100):
        if run(score, 3)==0:
            print(score, "CAN'T BE OBTAINED WITH THREE")
            break

#b() 61,81

def c():
    starts = [i*2 for i in range(1,21)]
    from itertools import product, combinations
    scores = defaultdict(set)
    for i in product(starts, [i for i in range(1,21)], [i for i in range(1,21)]):
        scores[sum(i)].add(i)

    ans = 0
    for i in scores:
        lst = list(scores[i])
        for item in combinations(lst, 2):
            if len(set(item[0]+item[1]))==6:
                ans += 1
    print(ans*2)

#c() 652600 - Incorrect


"""

SCORES 27/35





"""
