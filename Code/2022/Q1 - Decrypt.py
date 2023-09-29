
from itertools import product
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
look = {i:ord(i)-64 for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

s = input()

def decrypt(s):

    ans = []
    for i in range(len(s)-1, 0,-1):
        val = look[s[i]]-look[s[i-1]]
        if val < 0:
            val += 26
        ans.append(alpha[val-1])
    ans.append(s[0])
    return ans[::-1]


def b():
    for word in product(alpha, repeat=5):
        sword = list(word)
        #print(sword, decrypt(sword))
        if sword == decrypt(sword):
            print("Part b:", sword)
            return

def c():
    ### Encrypting until the same is the same as decrypting until the same

    print(find_cyle("OLYMPIAD"))

def find_cyle(s):
    c = 0
    orig = list(s)
    while c < 500:
        s = decrypt(s)
        #print(s, c)
        if s == orig:
            return c
        c += 1

def d():

    t = 0
    for s in product(alpha, repeat=3):
        clen = find_cyle(s)
        clen += 1
        if  999999999999%clen == 0:
            #print(s, clen)
            t += 1
    print(t)



print("".join(decrypt(s)))
#b() # z z z z a
c() # 103
d()
