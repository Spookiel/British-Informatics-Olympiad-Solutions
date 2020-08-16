



n = int(input())

def gen(n):
    odds = [i for i in range(1,n+50, 2)]


    for i in range(1,len(odds)):
        try:
            if odds[i]!=0:
                #print(odds[i], "FOUND")
                for j in range(odds[i]-1,len(odds), odds[i]):
                    #print("REMOVING", odds[j])
                    odds[j] = 0

                for i in range(len(odds)-1,-1,-1):
                    if odds[i]==0:
                        odds.pop(i)
        except:
            break
    return odds

odds = gen(n)
def solve(odds, n):
    ans = []
    odds = gen(n)
    c = 0
    while odds[c] < n:
        c += 1
    ans.append(odds[c-1])
    while odds[c]==n:
        c += 1
    ans.append(odds[c])
    return tuple(ans)

got = solve(odds, n)
print(" ".join(list(map(str, got))))
#print(odds)


def b():
    odds = gen(100)
    ans = 0
    for i in odds:
        if i < 100:
            ans += 1
    print(ans)

#b() -> 23

def c(test):
    odds = gen(20000)
    hun = odds[test-1]
    seen = set()
    for i in range(2, hun+1):
        got = solve(odds, i)
        seen.add(got)
    print(len(seen), test)
    #Rule is (2*n)-2


#c() -> 1,999,999,998





""" Driver code for part c
for h in range(100,1000, 10):
    c(h)"""

