#Solution by @Pararcana
river1, river3, river9 = [1], [3], [9]

def gen_rivers(river):
  while river[-1] < 25000:
    sumDigits = sum([int(x) for x in str(river[-1])])
    river.append(river[-1] + sumDigits)

gen_rivers(river1)
gen_rivers(river3)
gen_rivers(river9)

k = int(input("Enter a river: "))

while True:
  if k in river1:
    print("Meets river 1 at " + str(k))
    break
  elif k in river3:
    print("Meets river 3 at " + str(k))
    break
  elif k in river9:
    print("Meets river 9 at " + str(k))
    break
  k += sum([int(x) for x in str(k)])
