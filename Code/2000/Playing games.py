import time
n = int(input())
d1 = list(map(int, input().split()))
d2 = list(map(int, input().split()))

start = time.time()

d1.sort()
d2.sort()

d1 = tuple(d1)
d2 = tuple(d2)


from itertools import combinations_with_replacement, combinations


def calc(d1, d2):
    ### Returns the fairness list

    ans = [0 for _ in range(25)]
    for i in d1:
        for j in d2:
            ans[i+j] += 1
    return ans

targ = calc(d1, d2)


def fill(cur, target, d1,turns, cdice = []):
    ### Use the list format for frequencies

    if turns == 0:

        return cur == target and all([val > 0 for val in cdice]), cdice

    cpos = len(cur)-1
    flag = False
    while cur[cpos] == target[cpos] and cpos > 0:
        cpos -= 1
        if cur[cpos] > target[cpos]:
            flag = True
            break
    if flag: return False,[] ### Too many of a certain element



    ### Find the number of times max of d1 appears in d1
    maxelem = max(d1)
    freq_of_max =  d1.count(maxelem)
    if freq_of_max <= target[cpos]-cur[cpos]:
        elem_req = cpos-maxelem

        for odig in d1:
            cur[odig+elem_req] += 1

        ### Recurse here
        res, vdie = fill(cur, target, d1, turns-1, cdice+[elem_req])

        if not res:
            ### Undo changes
            for odig in d1:
                cur[odig + elem_req] -= 1
        else:
            return True, vdie
    return False, []





def run():



    str = list(combinations_with_replacement([i for i in range(1, 10)], r=n))
    for p1 in str:

        ### Can fill in the second dice recursively

        can, ans = fill([0 for i in range(25)], calc(d1, d2), list(p1), n)

        ans = tuple(sorted(ans))

        if can and ans and not (tuple(p1) == d1 and ans == d2 or tuple(p1) == d2 and ans == d1): ### Check the solution found is not the input
            return p1, list(ans)
    return False



res = run()
if not res:
    print("IMPOSSIBLE")
else:
    a,b = res
    print(*list(a))
    print(*sorted(b))
print(time.time()-start, "SECONDS")