
d = int(input())

s = [int(i) for i in input()]


def swap(serial):
    got = []
    serial = list(serial)
    for i in range(1, len(serial)):
        cserial = serial[:]
        #print("TRYING TO SWAP", i, i-1, cserial, cserial[i-1], cserial[i])
        for j in [-2,1]:
            new = i+j
            if new >= 0 and new < len(serial):
                if len(set([new, i, i-1]))==3:
                    if serial[i] < serial[new] < serial[i-1] or serial[i] > serial[new] > serial[i-1]:
                        #print("FOUND", serial[new], serial[i], serial[i-1], new, i)
                        cserial[i],cserial[i-1] = cserial[i-1],cserial[i]
                        break
        if cserial!=serial:
            got.append(tuple(cserial))
    return got

def bfs(start, targ=None):
    seen = set()
    queue = [(start, 0)]
    while queue:
        ne, dist = queue.pop(0)
        #print(ne, dist)
        seen.add(ne)
        for can in swap(ne):
            if can == targ:
                return dist+1, seen

            if can not in seen:
                queue.append((can, dist+1))
                seen.add(can)
    return dist,seen
import time
startTime = time.time()
ans = bfs(tuple(s))
print(ans[0])
print("COMPLETED IN", time.time()-startTime)

def b():
    first = "326451"
    second = "183654792"
    first = [int(i) for i in first]
    second = [int(i) for i in second]
    for item in [first, second]:
        dist, seen = bfs(tuple(item))
        ma = 0
        for it1 in seen:
            for it2 in seen:
                got = bfs(it1, it2)[0]
                ma = max(ma, got)
        print(ma)

# b() -> 7, 16

def c():
    from itertools import permutations
    import time
    startTime = time.time()
    for num in [6,10]:
        searching = set(permutations(range(1, num)))
        got = 1
        while searching:
            ne = searching.pop()
            searching -= bfs(ne)[1]
            if searching:
                got += 1
            #print(got)
        print(got, "FOR", num-1)
    print("Completed in", time.time()-startTime)
c()
