
def solve(inp):
    left = [1,0]
    right = [0,1]

    for i in inp:
        if i=="L":
            left = [left[0]+right[0], left[1]+right[1]]
        else:
            right = [left[0]+right[0], left[1]+right[1]]
        #print(left, right)

    ans = [left[0]+right[0], left[1]+right[1]]
    return f"{ans[0]} / {ans[1]}"

print(solve(input()))

#b() -> LRRR

def c():
    for i in range(1,10):
        print(solve("L"*i), i)

#c() -> 999,999