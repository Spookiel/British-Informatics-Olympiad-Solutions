from functools import lru_cache


@lru_cache(maxsize=None)
def check(string):
    if len(string)==1:
        return True
    if len(string)==2:
        if check(string[0]) and check(string[1]) and string[0] > string[1]:
            return True
        return False
    for pos in range(1,len(string)):
        left, right = string[:pos], string[pos:]
        #print(left, right)

        #if reverse of left and right are both pats

        if check(left[::-1]) and check(right[::-1]):
            got = max(right)
            flag = True
            for char in left:
                if char <= got:
                    flag = False
            if flag:
                return True
    return False


from itertools import permutations
counter = 0
alpha = "ACDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(1,len(alpha)):
    for perm in permutations(alpha[:i]):
        got = check("B"+"".join(perm))

        if got:
            counter += 1
    print(counter, i)