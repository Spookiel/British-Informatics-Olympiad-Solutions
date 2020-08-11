

n = int(input())

import time
start = time.time()



def sieve(ubound):
    primes = [True for i in range(ubound+1)]
    ret = set()
    for i in range(2, len(primes)):
        if primes[i]:
            ret.add(i)
            for j in range(2*i, len(primes), i):
                primes[j] = False
    return ret

primes = sieve(1000001)
def primef(n, ans = set()):
    if n==1:
        return ans
    else:
        for i in primes:
            if n%i==0:
                ans.add(i)
                return primef(n//i, ans)


def solve(n):
    a = primef(n, set())
    #print(a, n, "HERE")
    tot = 1
    for i in a:
        tot *= i

    return tot


print(solve(n))


def b():

    done = 0
    for i in range(1, 1000):

        if solve(i)==10:
            done += 1
            print(i, "HERE", solve(i))
        if done==10:
            break
#b) -> 10,20,40,50,80,100,160,200,250,320



def c():
    from collections import defaultdict
    scores = defaultdict(int)

    for i in range(1, 1000001):
        a = solve(i)
        if i%10000==0:
            print(i)
        scores[a] += 1
    print(max(scores, key=lambda x: scores[x]))
#c()
#c) -> 210
