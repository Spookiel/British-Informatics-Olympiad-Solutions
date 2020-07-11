



#1 -> 2341567
#2 -> 1237456
#3 -> 4123567
#4 -> 1235674

def one(shirts):
    return shirts[1:4]+shirts[0]+shirts[4:]

def two(shirts):
    return shirts[:3]+shirts[-1]+shirts[3:6]

def three(shirts):
    return shirts[3]+shirts[:3]+shirts[-3:]

def four(shirts):
    return shirts[:3]+shirts[-3:]+shirts[3]

assert one("1234567") == "2341567"
assert two("1234567") == "1237456"
assert three("1234567")=="4123567"
assert four("1234567")=="1235674"

funcs = [one, two, three, four]

def bfs(start, target="1234567"):
    seen = set()
    queue = [(start,0)]
    while queue:
        ne,dist = queue.pop(0)
        if ne == target:
            return dist

        seen.add(ne)
        for func in funcs:
            new = func(ne)
            if new not in seen:
                queue.append((new, dist+1))
                seen.add(new)


start = input()
print(bfs(start))

def b(opers):
    from itertools import product
    seen = set()
    for order in product(funcs, repeat=opers):
        shirts = "1234567"
        for o in order:
            shirts = o(shirts)
        seen.add(shirts)
    print(len(seen))


#b) b(2) -> 11, b(6) -> 403

def c():
    from itertools import permutations

    m = 0
    ans = None
    for p in permutations("1234567"):
        p = "".join(p)
        a = bfs(p)
        if a > m:
            m = a
            ans = p
    print(m, ans)
#c() -> 14,5674321


""" d)
No, if 1234567 is reachable from any other point, all other points are reachable
therefore if the maximum distance to 1234567 is 14, then the maximum distance between any two points has to be less than or equal to 14
This is because if the distance were any greater than 14, then the maximum distance between 1234567 and one of the points would be greater than 14 too


"""