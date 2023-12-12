#Solution by @Pararcana
numerals = [
    ["", "M", "MM", "MMM"],
    ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
    ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
    ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
]

def roman_splitter(roman):
  roman = "".join(roman) + " "
  spl = []
  counter = 1
  for i in range(len(roman) - 1):
    if roman[i] != roman[i + 1]:
      spl.append(roman[i]*counter)
      counter = 1
    else:
      counter += 1
  return spl

def roman_to_int(num):
  ans = []
  for i, v in enumerate(num):
      ans.append(numerals[i][int(v)])
  return "".join(ans)

def step(inpArr):
  outArr = []
  inpArr = roman_splitter(inpArr)
  for i in range(len(inpArr)):
    outArr.append(roman_to_int("{:04d}".format(len(inpArr[i]))))
    outArr.append(inpArr[i][0])
  return outArr

roman, repeat = input("Input Roman Numerals and a number: ").split()
roman, repeat = list(roman.upper()), int(repeat)

for _ in range(repeat):
  roman = step(roman)
roman = "".join(roman)
print(roman.count("I"), roman.count("V"))
