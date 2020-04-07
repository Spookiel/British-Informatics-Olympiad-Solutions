with open("Q1.in", "r") as fin:
    d = {}
    rd = {}
    for i in range(3):
        lines = fin.readline().split()
        pairs = [lines[i:i+2] for i in range(0, len(lines), 2)]
        for p in pairs:
            a,b = p
            d[int(a)] = b
            rd[b] = a

def convertTo(num):
    ans = ""
    for i in str(num):
        ans += d[int(i)]
    return ans

def convertFrom(string):
    pairs = "".join([rd[string[i:i+2]] for i in range(0, len(string), 2)])
    return int(pairs)

print(convertFrom(input("ENTER NUMBER: ")))

#1b)
#print(convertTo(convertFrom("sovo")+convertFrom("rexa")))
# = pareno


""" Part 1c) - vobi

def sumAlpha(string):
    return sum([ord(i)-96 for i in string])
for i in range(1,1000):
    if sumAlpha(convertTo(i))==i:
        print(convertTo(i), i)
        break"""


"""SCORES FULL CREDIT 28/28"""
