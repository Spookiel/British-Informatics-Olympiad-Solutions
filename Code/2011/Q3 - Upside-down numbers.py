

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


scores = [1, 9]
c= 2
tot = 10
while tot < n:
    tot += scores[(len(scores) - 2)] * 9
    scores.append(scores[(len(scores)-2)]*9)

print(scores)