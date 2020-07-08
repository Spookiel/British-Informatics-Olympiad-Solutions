
from collections import Counter
nums = list(map(int, input().split()))

from math import comb

from itertools import combinations, combinations_with_replacement

ans = 0
for i in range(1, 6):
    for j in combinations(nums, r=i):
        if sum(j)==15:
            ans += 1

c = Counter(nums)
for i in c:
    if c[i] > 1:
        ans += comb(c[i],2)
print(ans)


#b) 2 4 6 8 10


def c():
    ans = 0
    for i in combinations_with_replacement(range(1,11), r=5):
        if sum(i)==15 and len(set(i)) >= 2:
            #print(i)
            ans += 1
    print(ans)
#c() -> 28

"""
SCORES FULL MARKS 30/30




"""


