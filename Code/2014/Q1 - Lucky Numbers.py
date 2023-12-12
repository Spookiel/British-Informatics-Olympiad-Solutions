#Solution by @Pararcana
lucky = [i for i in range(1, 10005, 2)]
n = 3

for _ in range(168):
  luckyNew = []
  for i, v in enumerate(lucky):
    if (i+1) % n != 0:
      luckyNew.append(v)
  lucky = luckyNew.copy()
  n = lucky[lucky.index(n) + 1]

num = int(input("Enter a number: "))

highest = max([v for v in lucky if v < num])
lowest = min([v for v in lucky if v > num])

print(highest, lowest)

#Rest by Spookiel
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

