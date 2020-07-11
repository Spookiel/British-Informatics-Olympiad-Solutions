

s = list(input())


words = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

wdic = {i:words[i-1] for i in range(1,10)}
flag = False
for i in wdic:

    found = [False]*len(wdic[i])
    pos = 0
    for let in range(len(s)):
        if s[let]==wdic[i][pos]:
            if pos==0:
                found[pos] = True
                pos += 1
            else:
                if found[pos-1]:
                    found[pos] = True
                    pos += 1
        if all(found):
            print(i)
            flag = True
            break
    if flag:
        break

if not flag:
    print("NO")



def b():
    import re
    # No. of ways of making two from subsequences

    prefix = [[0,0,0]]*9
    targ = "TWOTWOTWO"
    from itertools import permutations,combinations
    counter = 0
    for perm in combinations(targ, 3):
        if "".join(perm)=="TWO":
            counter += 1
    print(counter)


#b) b() -> 10

#c)


def c():
    lets = set("".join(words[:5]))
    print(lets)
    lets = set("".join(words))
    print(lets)


c()

#12,16