
from math import ceil

a = int(input())
b = int(input())



def calc_pairs(num, denom):


    best = [999999,999999]
    for c in range(1,32001):
        x = (num/denom)-(1/c)
        d,e = x.as_integer_ratio()
        if d==1:
            if min([c,e]) < min(best):
                best = [c,e]

    print(best)

from fractions import Fraction

def find_next(f1: Fraction):

    num, denom = f1.as_integer_ratio()
    bval = ceil(denom/num)

    return bval, f1-Fraction(1, bval)


fr = Fraction(a,b)
nums = []


while 1:

    val, fr = find_next(fr)
    nums.append(val)
    if fr == 0:
        break
print(*nums)


