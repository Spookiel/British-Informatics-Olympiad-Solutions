#Solution by @Pararcana
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
factors1, factors2 = [], []

def factoriser(arr, num):
  for i in range(num):
    if num%(i+1) == 0 and i+1 != num:
      arr.append(i+1)


def adder(arr):
  total = 0
  for item in arr:
    total += item
  return total


factoriser(factors1, num1)
factoriser(factors2, num2)


if (adder(factors1) == num2) and (adder(factors2) == num1):
  print("Amicable numbers.")
else:
  exit()

print("".join(decrypt(s)))
#b() # z z z z a
c() # 103
d()
