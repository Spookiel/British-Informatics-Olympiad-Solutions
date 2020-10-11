

n = int(input())


def check(n):
    for i in range((len(str(n))//2)+1):
        if int(str(n)[-i-1])+int(str(n)[i])!=10:
            return False
    return True



def brute(n):
    c = 0

    cur = 1
    while True:
        if check(cur):
            yield cur
            c += 1
        if c==n:
            break
        cur += 1

first = [i for i in brute(30)]


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

#) c() -> 38