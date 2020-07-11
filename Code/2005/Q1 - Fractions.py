from math import gcd


n = float(input())

def solve(n):

    for i in range(2,10001):
        test = n*i
        if int(test)==test:
            #print(int(test), "/", i)
            break
    test = int(test)
    g = gcd(test, i)
    test //= g
    i //= g
    return int(test), i

print("/".join(list(map(str,solve(n)))))



def b():
    seen = set()
    for i in range(1,10000):
        go = i/10000
        #print(go)
        seen.add(solve(go)[1])
    print(len(seen))

#b() 24




def c():
    best = -1
    ans = None
    for i in range(1, 10000):
        go = i/10000
        tot = 1
        nom,denom = solve(go)
        for k in str(nom):
            tot *= int(k)
        for j in str(denom):
            tot *= int(j)

        #print(tot, go, i)
        if tot > best:
            ans = go
            best = tot
    print(ans, best, solve(ans))
# c() 0.9584



"""SCORES FULL MARKS 30/30
    
    The idea here is quite simple, the fraction a/b is equal to some decimal, which we are given as in input
    We know that b has to be some number between 2 and 10000 inclusive, therefore we can just brute force all numbers between
    2 and 10001
    
    therefore
    
    a = decimal*b
    So if a is an integer, then we know a and b are both integers, and therefore we have found a valid match
    
    now that we have a, b we need to make sure the fraction a/b can't be simplified further.
    
    To do this, we take the Greatest Common Divisor (GCD) of a and b, and divide a by the GCD(a, b) and divide b by GCD(a, b)
    this makes sure that the fraction a/b can't be simplified further

"""