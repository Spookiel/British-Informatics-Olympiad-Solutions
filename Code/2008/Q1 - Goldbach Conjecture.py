

n = int(input())



primes = [1 for i in range(10001)]
primes[0] = 0
primes[1] = 0
for num in range(2,len(primes)):
    if primes[num]:
        for j in range(2*num, len(primes), num):
            primes[j] = 0


def solve(n):
    counter = 0
    seen = set()
    for i in range(10001):
        if primes[i]:
            if i < n:

                if primes[n-i]:
                    seen.add(tuple(sorted([i, n-i])))
    #print(len(seen))
    return len(seen)

print(solve(n))


#b) 17,29,   23,23,   3,43   ,5,41


def c():
    count = 0
    for i in range(5,50, 2):
        if solve(i) == 0:
            count += 1
    print(count)

#c() -> 9