import heapq as heapq
import time
from itertools import combinations
"""Key notes:
There is no point sending an astronaut over on their own
Pairing the largest astronaut with the smallest is not necessarily optimal
Pairing the middle two astronauts is not necessarily optimal

This naturally leads to a BFS/Brute force approach for this problem,
however the implementation is a bit messy. 
"""


n = int(input())
origAstros = list(map(int, input().split()))
start = time.time()
state = (n,0,[],origAstros, False) #Astros on the station, outside, time taken, oxygen tank on the station
queue = [state]

def get_possible(state):
    global origAstros
    thing,time,station,outside, tank = state
    if not tank:
        if len(outside)==1:
            yield (n*100+time+outside[0],time+outside[0], outside+station, [], not tank)
        for pair in combinations(outside, 2):
            cTime = int(time)
            cStation,cOutside = station[:], outside[:]
            cTime += max(pair)
            cStation.append(pair[0])
            cStation.append(pair[1])
            cOutside.remove(pair[0])
            cOutside.remove(pair[1])
            yield ((n-len(cStation))*100+cTime,cTime, cStation, cOutside, not tank)
    else:
        for pos in station:
            cTime = int(time)
            cStation,cOutside = station[:], outside[:]
            cTime += pos
            cStation.remove(pos)
            cOutside.append(pos)
            yield ((n-len(cStation))*100+cTime,cTime,cStation, cOutside, not tank)

def runBrute():
    start = time.time()
    state = (n,0,[],origAstros, False) #Astros on the station, outside, time taken, oxygen tank on the station
    queue = [state]
    flag = False
    out = True
    best = 99999
    c = 0
    while queue and not flag:
        c += 1
        if time.time()-start > 5:
            out = False
            print("BRUTE TIMED OUT AFTER", c, "ITERATIONS")
            break
        state = queue.pop(-1)
        if state[1] >= best:
            continue
        for m in get_possible(state):
            if not m[3] and m[1] < best:
                best = m[1]
                #print(best)
            else:
                queue.append(m)
    if out:
        print("GOT ANSWER", best, "IN", time.time() - start, "WITH", c, "ITERATIONS")
#This basic BFS approach ends up scoring 21/30, but we can do better see below for an even quicker solution
def runBetter():
    start = time.time()
    state = (n,0,[],origAstros, False) #Astros on the station, outside, time taken, oxygen tank on the station
    queue = [state]
    heapq.heapify(queue)
    flag = False
    best = 99999
    c = 0
    while queue and not flag:
        state = heapq.heappop(queue)
        c += 1
        if state[1] >= best:
            continue
        if time.time()-start > 0.9:
            break
        for m in get_possible(state):
            if not m[3] and m[1] < best:
                best = m[1]
            elif m[1] <= best:
                if not queue or m not in queue:
                    heapq.heappush(queue, m)
    print("GOT ANSWER", best,"IN",time.time()-start,"WITH", c, "ITERATIONS")
#Using HeapQ and some heuristics, we can get 30/30

"""Analysis:
It is very possible to get it done without heuristics, but by realizing that we should prioritise the states with
more astronauts on the station, and prioritise the states which are currently on less time, we can find a solution very quickly.

Another way to consider this problem, is by thinking about it as a graph, and using a graph traversal such as Djikstra's to traverse
it. Such a solution is shown below.




"""

def runFast():
    # Side is true if pack is on the right
    queue = [(0, [], origAstros, True)]
    heapq.heapify(queue)
    tstart = time.time()
    flag = False
    calls = 0
    minFound = 9999
    seen = {}
    def make(left,right,side):
        return (tuple(sorted(left)), tuple(sorted(right)),side)
    while queue and not flag:
        calls += 1
        times, left, right, side = heapq.heappop(queue)
        abcd = make(left,right, side)
        if calls%10000==0:
            print("DONE", calls, len(queue))
        seen[abcd] = min([seen.get(abcd, 99999), times])
        if side:
            if len(right) > 1:
                for pair in combinations(right, 2):
                    a, b = pair
                    cleft, cright = left[:],right[:]
                    cright.remove(a)
                    cright.remove(b)
                    cleft.append(a)
                    cleft.append(b)
                    abc = make(cleft, cright,not side)
                    if times + max([a, b]) < seen.get(abc, 9999):
                        if times + max([a, b]) < minFound:
                            seen[abc] = min([seen.get(abc, 99999), times + max([a, b])])
                            heapq.heappush(queue, (times + max([a, b]), cleft, cright, not side))
            else:
                for p in right:
                    cleft, cright = left[:],right[:]
                    cright.remove(p)
                    cleft.append(p)
                    abc = make(cleft, cright,not side)
                    if times + p < seen.get(abc, 9999):
                        if times +p < minFound:
                            seen[abc] = min([seen.get(abc, 99999), times +p])
                            heapq.heappush(queue, (times +p, cleft, cright, not side))
        else:
            if len(right) == 0 and times < minFound:
                print("GOT ANSWER OF", times, "IN", time.time() - tstart, "WITH", calls, "ITERATIONS")
                flag = True
                minFound = times
            else:
                for t in left:
                    cleft, cright = left[:],right[:]
                    cleft.remove(t)
                    cright.append(t)
                    bc = make(cleft, cright, not side)
                    if times+t < seen.get(bc, 9999):
                        if times + t < minFound:
                            seen[bc] = min([seen.get(bc, 9999), times+t])
                            heapq.heappush(queue, (times + t, cleft, cright, not side))
runBrute()
runBetter()
runFast()

