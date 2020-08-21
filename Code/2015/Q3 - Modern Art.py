from math import factorial

a,b,c,d,n = list(map(int, input().split()))



def perm(a,b,c,d):
    return factorial(a+b+c+d)//(factorial(a)*factorial(b)*factorial(c)*factorial(d))

def solve(a,b,c,d,n):
    if a+b+c+d==0:
        return ""
    #print(a,b,c,d,n)
    #input()
    if a > 0:
        wayA = perm(a-1,b,c,d)
        #print(f"There are {wayA} ways to arrange {a},{b},{c},{d},{n} starting with A")
        if wayA >= n:
            return "A"+solve(a-1,b,c,d,n)
        n -= wayA
    if b > 0:
        wayB = perm(a, b-1,c,d)
        #print(f"There are {wayB} ways to arrange {a},{b},{c},{d},{n} starting with B")
        if wayB >= n:
            return "B"+solve(a,b-1,c,d,n)
        n -= wayB
    if c > 0:
        wayC = perm(a,b,c-1,d)
        #print(f"There are {wayC} ways to arrange {a},{b},{c},{d},{n} starting with C")
        if wayC >= n:
            return "C"+solve(a,b,c-1,d,n)
        n -= wayC

    return "D"+solve(a,b,c,d-1,n)

print(solve(a,b,c,d,n))


def b():
    #Binary search - Could do it by hand, but here is the code for completeness
    targ = "AABCCBDD"
    low = "".join(sorted(targ))
    high = low[::-1]
    lnum = 1
    hnum = perm(2,2,2,2)
    while lnum < hnum:
        mnum = (lnum+hnum)//2
        got = solve(2,2,2,2,mnum)
        if got == targ:
            print(mnum)
            break
        elif got < targ:
            lnum = mnum+1
        else:
            hnum = mnum
#b() -> 10


