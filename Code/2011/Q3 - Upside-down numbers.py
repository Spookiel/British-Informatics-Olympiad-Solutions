n = int(input())
import time
#print(2**1000)

start = time.time()
scores = [0,1,9]
c= 2
tot = 10
while tot < n:
    tot += scores[(len(scores) - 2)] * 9
    scores.append(scores[(len(scores)-2)]*9)

#print(scores)

ans = ["0" for i in range(len(scores)-1)]
if n==1:
    print(5)
else:
    n -= sum(scores[:-1])

    for place in range(len(ans)//2):
        totalFor = 0

        startsEach = scores[len(ans)-(2*place)]//9

        #print(place, startsEach, n)


        for digit in range(1, 10):
            totalFor += startsEach
            if n <= totalFor:
                ans[place] = str(digit)
                ans[-place-1] = str(10-digit)
                n -= totalFor-startsEach
                break

    if len(ans)%2==1:
        ans[len(ans)//2] = "5"
    print("".join(ans))
    print("FINISHED IN", time.time()-start)


def b():
    count = 0
    from itertools import permutations
    for pos in permutations(list(map(str, range(1, 10)))):
        count += 1 if check("".join(pos)) else 0
    print(count, "PART B")

#) b() -> 384

def c():
    targ = 1e18
    scores = [0, 1, 9]
    c = 2
    tot = 10
    while tot < targ:
        tot += scores[(len(scores) - 2)] * 9
        scores.append(scores[(len(scores) - 2)] * 9)

    print(len(scores)-1)



