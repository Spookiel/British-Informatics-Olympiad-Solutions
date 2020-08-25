from math import log2,floor
from collections import defaultdict
def sieve(upper):
    got = [True for i in range(upper+1)]
    got[0] = False
    got[1] = False
    for num in range(2, upper+1):
        if got[num]:
            for j in range(2*num, upper+1, num):
                got[j] = False
    return got

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True



def bi_bfs(start, end, lim):
    loglim = floor(log2(lim))
    both = [[[(start, 0)], defaultdict(int)], [[(end, 0)], defaultdict(int)]]
    switch = 0
    both[0][-1][start] = 0
    both[1][-1][end] = 0
    while True:
        cq, cs = both[switch]
        ne, dist = cq.pop(0)
        #cs[ne] = dist
        for power in range(loglim+1):
            twopow = 2**power
            if ne > twopow:
                lowprime = ne-twopow
                if isPrime(lowprime) and lowprime not in cs:
                    cq.append((lowprime, dist+1))
                    cs[lowprime] = dist+1

            highprime = ne+twopow
            #print(highprime, ne,dist, "HERE")
            if isPrime(highprime) and highprime not in cs and highprime <= lim:
                cs[highprime] = dist+1
                cq.append((highprime, dist+1))

        #print(both[0][-1], both[1][-1])
        if (ans := set(both[0][-1].keys())&set(both[1][-1].keys())):
            overlap = ans.pop()
            #print(overlap)
            finalans = both[0][-1][overlap]+both[1][-1][overlap]+1
            print(finalans)
            #print(both[0][-1])
            #print(both[1][-1])
            break

        switch = 1 - switch

lim, start, end = list(map(int, input().split()))



import time
starttime = time.time()
bi_bfs(start, end, lim)
#print(time.time()-starttime, "COMPLETED IN")




