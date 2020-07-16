n = int(input())

def check(n):
    n = str(n)
    for i in range((len(n)//2)+1):
        if int(n[i])+int(n[-i-1])!=10:
            return False
    return True

def brute(n):
    ans = [5]
    cur = 10
    while len(ans) < n:
        if check(cur):
            ans.append(cur)
        cur += 1
    return ans

print(brute(n))
