


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
            #print(got, right, string)
            flag = True
            for char in left:
                if char <= got:
                    flag = False
            if flag:
                #print("found", left, right, "for", string)
                return True
    return False
from itertools import permutations

def isPat(a):
    if len(a)==1:
        return True
    for x in range(1, len(a)):
        l, r = a[:x], a[x:]
        if all(i>j for i in l for j in r):
            if isPat(l[::-1]) and isPat(r[::-1]):
                return True
    return False

for perm in permutations("ABCD"):
    perm = "".join(perm)
    if isPat(perm):
        print(perm)