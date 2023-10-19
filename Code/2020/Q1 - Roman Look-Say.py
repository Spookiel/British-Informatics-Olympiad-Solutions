roman, repeat = input("Input Roman Numerals and a number: ").split()
roman, repeat = list(roman.upper()), int(repeat)
numerals = [
["M", ""],
["C", "D", "M", ""],
["X", "L", "C", ""],
["I", "V", "X", ""]
]
cast = [[-1], [0], [0,0], [0,0,0], [0,1], [1], [1,0], [1,0,0], [1,0,0,0], [0,2]]

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
  for i, n in enumerate(num):
    for j in range(len(cast[int(n)])):
      ans.append(numerals[i][cast[int(n)][j]])
  return "".join(ans)

for _ in range(repeat):
  romanTemp = []
  roman = roman_splitter(roman)
  for i in range(len(roman)):
    romanTemp.append(roman_to_int("{:04d}".format(len(roman[i]))))
    romanTemp.append(roman[i][0])
  roman = romanTemp.copy()

roman = list("".join(roman))
print(roman.count("I"), roman.count("V"))
