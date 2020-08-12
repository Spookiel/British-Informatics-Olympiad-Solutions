

n,m = list(map(int, input().split()))


def solve(n,m, debug=False):
    c1 = [0,0]
    c2 = [0,0]
    tot = 0
    while True:
        c1[1] += n
        c2[1] += m
        c1[0] += c1[1]//60
        c1[1] %= 60
        c1[0] += 1
        c1[0] %= 24
        c2[0] += c2[1]//60
        c2[1] %= 60
        c2[0] += 1
        c2[0]%=24
        tot += 1
        if c1==c2:
            break
    ans = [("0" if len(str(c1[0])) < 2 else "")+str(c1[0]), ("0" if len(str(c1[1])) < 2 else "")+str(c1[1])]
    if not debug:
        print(":".join(ans))
    return c1, tot

solve(n,m)


def b():
    for i in range(20):
        print(solve(0, i,debug=True), i)

# b) -> 0, 8, 9, 16, 18



def c():
    best = 0
    for i in range(400):
        print(i)
        for j in range(400):
            useless, hours = solve(i,j, debug=True)
            if hours > best:
                best = hours
    print(best, "PART C")

#c) 1440 hours
