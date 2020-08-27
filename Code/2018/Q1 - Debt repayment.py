
from math import ceil,floor
r,p = list(map(int, input().split()))
r *= 0.01
p *= 0.01

done = 0
amount = 10000
while amount > 0:
    debt = ceil(round(amount*r, 6))
    #print(amount*r,debt, "HERE")
    amount += debt
    toPay = ceil(round(amount*p, 6))
    if toPay < 5000:
        toPay = 5000
    if amount < toPay:
        toPay = amount
    done += toPay
    amount -= toPay
    #print(done, amount, toPay)
#print(amount, toPay/100)
print(done/100)


