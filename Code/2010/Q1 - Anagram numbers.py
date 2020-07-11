
n = int(input())

from collections import Counter

def solve(n, debug=False):
    flag = False
    ans = []
    for i in range(2,10):
        check = n*i
        check = str(check)
        if Counter(check)==Counter(str(n)):
            if not debug:
                print(i, end=" ")
            else:
                ans.append(i)
            flag = True

    if not flag and not debug:
        print("NO")
    return ans

solve(n)
def b():
    print("SOLVING B")
    m = 85247910
    for num in range(2, 10):
        if m%num==0:
            check = m//num
            if Counter(str(check))==Counter(str(m)):
                print(check, num)
    print("\nEND OF B")

#Rb()
#b) -> 28415970,17049582,14207985


def c():
    counter = 0
    for num in range(100000,1000000):
        if solve(num, debug=True):
            if len(set(str(num)))==6:
                print(num)
                counter += 1
    print("C:", counter)

#c()

#c) -> 138