

n = int(input())





def sieve(ubound):
    primes = [True for i in range(ubound+1)]
    for i in range(2, len(primes)):
        if primes[i]:
            for j in range(2*i, len(primes), i):
                primes[j] = False
    return primes


def primef(n):
    primes = sieve(1000001)

primef(n)


print()