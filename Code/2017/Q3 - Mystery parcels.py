
#ONLY SCORES 8/20
arr = [1,1,1,3]


def solve(ar, i, target, parts,partArr=[]):
    #print(ar, i, target, parts, partArr)
    if not partArr:
        partArr = [[] for i in range(parts)]


    if i >= len(ar):
        return (False, [])
    val = ar[i]
    for k in range(len(target)):
        if target[k] >= val:
            target[k] -= val
            partArr[k].append(val)
            if solve(ar, i+1, target, parts, partArr)[0]:
                return (sum(target) == 0, partArr)

            else:
                try:
                    partArr.remove(val)
                    target[k] += val
                except Exception as e:
                    #print(e, partArr, val)
                    pass
    return (sum(target)==0, partArr)

#ans = solve(arr, 0, [3,3], 2)

p,i,n,w = list(map(int,input().split()))
from itertools import combinations_with_replacement, permutations




seen = set()
for i in combinations_with_replacement(range(1,i+1), n):
    got = solve(list(i), 0, [w]*p, p)
    items = sum([len(i) for i in got[1]])
    if got[0] and items==n:
        final = got[1]
        final = sorted([tuple(sorted(j)) for j in final])
        seen.add(tuple(final))


ans = 0
for i in seen:
    #print(list(permutations(i)))
    ans += len(set(permutations(i)))
print(ans)