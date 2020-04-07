s = [i for i in input("ENTER ISBN: ")]
d = {str(i):i for i in range(10)}
d["X"] = 10
d["10"] = "X"

def score(s):
    total = 0

    for i in range(len(s)):
        total += (10-i)*d[s[i]]
    #print(total, total%11==0)
    return total%11==0

pos = s.index("?")

for p in range(11):
    s[pos] = str(d[str(p)])
    #print("".join(s))
    if score(s):
        print(d[str(p)])
        break

"""SCORES FULL CREDIT 24/24
Watch the problem with 

"""