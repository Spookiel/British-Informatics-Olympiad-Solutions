


s = input()
t = input()

if sorted(s)==sorted(t):
    print("Anagrams")
else:
    print("Not anagrams")



#b) 3! - 6 ways


def c():
    from itertools import product
    seen = set()
    for i in product("ABC", repeat=5):
        i = sorted(i)
        seen.add(tuple(i))
    print(len(seen))

#c() 21


"""
SCORES FULL MARKS 30/30
"""