

n,s = input().split()

n = int(n)

from string import ascii_uppercase

alpha = ascii_uppercase

can = alpha[:n]

def check(string):
    for i in range(len(string)):
        for j in range(i+1,len(string)):
            for k in range(j+1, len(string)):
                if string[i] < string[j] < string[k]:
                    return False
    return True

from itertools import permutations



def brute(s):
    global can
    c = 0
    do = set(can)-set(s)
    s = list(s)
    for perm in permutations(do):
        if check(s+list(perm)):
            #print("".join(s+list(perm)))
            c += 1
    print(c)

#brute(s) Scores 12/24


def recurse(umin, omax, bet, rlen):


    if rlen==2 and omax > 0:
        return 0
    if rlen >= 3:
        return 0
    if umin==omax==bet==0:
        return 1
    total = 0
    for i in range(umin):
        total += recurse(i, omax, bet+1-i , rlen)

    for j in range(bet):
        total += recurse(umin, bet-1-j, j, rlen)

    for k in range(omax):
        total += recurse(umin, omax-k-1, k, rlen+1)

    print("SCORE FOR",umin, omax, bet, rlen, "IS", total)
    return total


def analyse(string):
    left = set(can)-set(string)
    mi = min(string)
    miState = len([i for i in left if i < mi])

    worst = ("Z", "Z", "Z")
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] < string[j]:
                if (store := (string[i], string[j])) < worst:
                    worst = (store[0], store[1], chr(ord("Z")+1))
            for k in range(j+1, len(string)):
                if string[i] < string[j] < string[k]:
                    if (store := (string[i], string[j], string[k])) < worst:
                        worst = store
    #print(worst)
    if worst==("Z","Z","Z"):
        omState = len([i for i in left if i > mi])
        rlenState = 1
        betState = len(left)-omState-miState
        return (miState, omState, betState, rlenState)
    else:
        if "[" in worst:
            rlenState = 2
            omState = len([i for i in left if i > worst[1]])
            betState = len(left)-omState-miState
            return (miState, omState, betState, rlenState)
        else:
            rlenState = 3
            return (-1,-1,-1,-1)



state = analyse(s)
if sum(state)==-4:
    print(0)
else:
    print(recurse(*state))






