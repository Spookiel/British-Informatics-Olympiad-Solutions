
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



"""Explanation:

This is a problem which can be solved using memoized recursion or dynamic programming. In this solution, I chose to use

a recursive function in order to better demonstrate the recurrence relation.

In this problem, to calculate the ways of arranging the blocks with a score of S
is the number of ways to arrange the blocks of 1 + score(S-1), 2 + score(S-2) ... S + score(0)

where score(0) = 1
and score(1) = 1

then all that remains is to iteratively build up the answer by trying each digit 1-9 as the next in the answer
if the ways of arranging that new sum is greater or equal to n, then that answer must be a prefix of it. For example

Say the target score is 4, and the arrangement we are looking for is 5.

Currently our answer is nothing
So we try starting answer with 1
We then call score(4-1) = score(3)
score(3) = 4
We are looking for the 5th arrangement 
5 > 4

n = 5 - 4
n = 1

now we try the digit 2
score(2) = 2
2 >= 1

so n stays as 1
and our answer is now 2 1

then we try 1 again

score(1) = 1

answer is 2 1 1

Now that the sum of answer is equal to the target sum, we stop













"""