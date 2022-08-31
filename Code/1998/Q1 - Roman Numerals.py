#Solution made by @Catatria
sep = []
ans = []
num = str(input("Input a number. "))

if 1 > num >= 4000:
  print("Error: Invalid number, above 4000 or below 1.")
  exit()

for i in range(4-len(num)):
  sep.append(0)
for i in range(len(num)):
  sep.append(int(num[i]))

romanNumerals = [["C", "D", "M"], ["X", "L", "C"], ["I", "V", "X"]]

for i in range(sep[0]):
  ans.append("M")

for i in range(3):
  if 3 >= sep[i+1] >= 1:
    for j in range(sep[i+1]):
      ans.append(romanNumerals[i][0])
  elif sep[i+1] == 4:
    ans.append(romanNumerals[i][0]+romanNumerals[i][1])
  elif sep[i+1] == 5:
    ans.append(romanNumerals[i][1])
  elif 8 >= sep[i+1] >= 6:
    ans.append(romanNumerals[i][1])
    for j in range(sep[i+1]-5):
      ans.append(romanNumerals[i][0])
  elif sep[i+1] == 9:
    ans.append(romanNumerals[i][0]+romanNumerals[i][2])
    
ans = "".join(ans)
print("\n"+ans)
