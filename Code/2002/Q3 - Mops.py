target = int(input())
arr = [99999 for i in range(0, target + 1)]
arr[0] = 0


def get_factors(num):
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            yield (n, num // n)


def getThing(num, arr):
    a = [arr[i[0]] + arr[i[1]] for i in get_factors(num)] + [99999]
    return min(a)


for i in range(1, target + 1):
    arr[i] = min([getThing(i, arr), arr[i - 1] + 1])
print(arr[target])

""" SCORES FULL CREDIT 24/24

This is a classic Dynamic Programming Problem, Or a different take on a classic one.

Let f(i) = min( f(Xj)+f(i/X) for X | i,
                f(i-1)+1)
                
Or more simply

For each mop, you can either +1 to the minimum way to get N-1, or find the sum of the ways to get to two factors of N

eg. Given 12
The possible ways,

        f(11)+1
        f(3)+f(4)
        f(6)+f(2)

This can be converted into a bottom-up DP approach via the following

arr = [9999 for i in range(target+1)]
arr[0] = 0

Let factors(n) return (X, n/x) For all X |n
for i in range(1,target+1):
    arr[i] = min(arr[i-1]+1, arr[i])
    for all factors of i:
        a,b = Factor1, i/Factor1
        arr[i] = min(arr[i], arr[a]+arr[b])
"""