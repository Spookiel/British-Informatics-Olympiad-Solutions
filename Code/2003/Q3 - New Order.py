
arr = [[0 for i in range(50)] for j in range(50)]

arr[0][1] = 1

for available in range(1,50):
    for ones in range(1,available+1):
        arr[available][ones] = arr[available-1][ones-1]+arr[available-1][ones]

from functools import lru_cache

#SCORES FULL MARKS 21/21


@lru_cache(maxsize=1024)
def score(available, left):
    if left==1:
        return available
    if available<=0:
        return 0
    if available==left:
        return 1
    if available==1 and left <0:
      return 0
    return score(available-1, left-1)+score(available-1, left)
n, ones = list(map(int, input().split()))
if ones!=0:
    length = 1
    while arr[length+1][ones+1] < n:
        length += 1
    answer = ""
    while len(answer) < length-1:
        addZero = arr[length-len(answer)][ones+1]
        addOne = arr[length-len(answer)][ones]
        if addZero >=n:
            answer += "0"
        else:
            n -= addZero
            ones -= 1
            answer += "1"
    if ones==1:
        answer += "1"
    else:
        answer += "0"

    if len(answer) <= 6:
        print(answer)
    else:
        print(" ".join([answer[i:i+6] for i in range(0, len(answer), 6)]))

else:
    print("0")

"""Analysis - Full credit solution

This is a DP (Dynamic Programming) problem once you break down the question and work out what they are asking.
One way to think about this problem is to consider the suffixes of a string of length n, for example, n=3

if n=3, then there are 4 strings of length n.
        100
        101
        110
        111
Now look at the last two characters - Half are ones, and half are zeros. This is True for any suffix of a string such that
the length is greater than 1

To start with this problem, we need to find a way of counting all the substrings which are N characters long and contain M ones
    How do we do this?
    One way to think about this is via a recursive formula. Say I'm computing all the strings of length N, with M ones.
    
    At each step, there are two choices, I can either choose a one to put in the string, or a zero. Then all that remains is to
    compute the number of strings which contain N-1 chars and M ones, and N-1 chars and M-1 ones, or, more mathematically - 
    
    Let f(N, M) be the number of strings of length N which have M ones in
    
    f(N, M) { 0 - N <= 0
              1 - M==1
              0 - M < 1
              f(N-1, M-1) + f(N-1, M)
    
    
    }





"""