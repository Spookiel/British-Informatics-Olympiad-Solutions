

s, n = input().split()
n = int(n)

### Calculate possible preferences for each car

def calc_possible(s):
    taken = set()
    tree = []
    for arrival in sorted(s):
        apos = s.index(arrival)
        ### Check every position before this to see if it's taken
        prefs = []
        for pos in range(apos-1,-1,-1):
            if pos in taken:
                prefs.append(pos)
            if pos not in taken and s[pos] > arrival:
                break
        tree.append(prefs[::-1]+[apos])
        taken.add(apos)
    return tree


from functools import lru_cache
@lru_cache(maxsize=None)
def calc_from(pos):
    if pos == len(tree):
        return 1
    return len(tree[pos])*calc_from(pos+1)





alpha = "ABCDEFGHIJKLMNOPQRSTUV"
ans = ""
depth = 0

tree = calc_possible(s)
while n > 0:

    for let in tree[depth]:
        from_here = calc_from(depth+1)
        if from_here >= n:
            ans += alpha[let]
            break
        else:
            n -= from_here
    depth += 1
    if depth == len(s):
        break
print(ans)