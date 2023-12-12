from fractions import Fraction
print(Fraction(input("Decimal: ")))


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
