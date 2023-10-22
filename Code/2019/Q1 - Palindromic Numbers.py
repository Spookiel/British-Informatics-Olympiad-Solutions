#Solution by @Pararcana
def makePalindrome(n):
  mid = len(n) % 2 != 0 and n[(len(n) - 1)//2] or ""
  palindrome = n[0:len(n)//2] + mid + n[(len(n)//2)-1::-1]
  return int(palindrome)

target = str(int(input("Enter a number: ")) + 1)
num = makePalindrome(target)

if len(target) == 1:
  print(target)
else:
  while num < int(target):
    sNum = str(num)
    num = makePalindrome(str(int(sNum[0:(len(sNum)+1)//2])+1) + sNum[(len(sNum)+1)//2:])
  print(num)

def b():
    ma = 0
    last = 1
    cur = 2
    while True:

        if (dif := cur-last) > ma:
            print(cur, last, dif, len(str(cur)))
            ma = dif
        last = int(cur)
        cur = int(solve(cur))
        if len(str(cur)) > 20:
            break
#b()

#b() -> 11,000,000,000

def c_helper(n,got):
    gotset = set(got)
    low = 0
    high = len(got)-1
    while True:
        mid = (high+low)//2
        if mid==low:
            break
        if got[mid] < n:
            low = mid
        else:
            high = mid-1
    n -= got[low]

    if n in gotset:
        print(n, got[low], n+got[low], "HERE")
        return True
    print("FAILED", n+got[low], got[low], got[high])
    return False


def c():
    got = []
    cur = 1
    while cur < 100000:
        got.append(cur)
        cur = int(solve(cur))

    for i in range(1,100):
        ans = c_helper(i, got)

    #10,000
#c()
