import time

from collections import deque,Counter,defaultdict


s = list(input())
s = deque(s)
steps, p = list(map(int, input().split()))
start = time.time()
for step in range(steps):
    new = deque()
    while s and len(new) < p:
        char = s.popleft()
        if char=="A":
            new.append("B")
        elif char=="B":
            new.append("A")
            new.append("B")
        elif char=="C":
            new.append("C")
            new.append("D")
        elif char=="D":
            new.append("D")
            new.append("C")
        else:
            new.append("E")
            new.append("E")
    s = new
    print(len(s), step)

got = defaultdict(int)
while p:
    got[s.popleft()] += 1
    p -= 1

for char in "ABCDE":
    print(got[char], end=" ")
print("\nCOMPLETED IN", end=" ")
print(time.time()-start)
