


alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
p,q,r = list(map(int, input().split()))

n = int(input())

MAXADJ = int(q)

from functools import lru_cache


@lru_cache(maxsize=None)
def countWays(curLetters, leftAdj,posLetters,lastLetter=-1):
    if leftAdj <= 0 or curLetters < 0:
        return 0
    if curLetters==0:
        return 1



    total = 0
    for letter in range(posLetters):
        total += countWays(curLetters-1, leftAdj-1 if letter == lastLetter else MAXADJ, posLetters, letter)
    return total


def solve(n, p,q,r):
    current = ""
    curAdj = int(q)
    while len(current) < r:

        for letter in alpha[:p]:
            ways = countWays(r-len(current)-1, q if not current or current[-1] != letter else curAdj-1, p, alpha.index(letter))
            #print(ways, letter, current)
            if ways < n:
                n -= ways
            else:
                if current:
                    if letter == current[-1]:
                        curAdj -= 1
                    else:
                        curAdj = q
                current += letter
                break
        #input()
    print(current)



solve(n,p,q,r)
