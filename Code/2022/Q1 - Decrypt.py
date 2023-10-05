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

#Rest by Spookiel
def b():
    for word in product(alpha, repeat=5):
        sword = list(word)
        #print(sword, decrypt(sword))
        if sword == decrypt(sword):
            print("Part b:", sword)
            return

def c():
    ### Encrypting until the same is the same as decrypting until the same

    print(find_cyle("OLYMPIAD"))

def find_cyle(s):
    c = 0
    orig = list(s)
    while c < 500:
        s = decrypt(s)
        #print(s, c)
        if s == orig:
            return c
        c += 1

def d():

    t = 0
    for s in product(alpha, repeat=3):
        clen = find_cyle(s)
        clen += 1
        if  999999999999%clen == 0:
            #print(s, clen)
            t += 1
    print(t)
  
#b() # z z z z a
c() # 103
d()
