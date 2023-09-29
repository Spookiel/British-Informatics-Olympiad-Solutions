#Solution by @Pararcana
denary = []
lojbanDict = {
  "no": "0", "pa": "1",
  "re": "2", "ci": "3",
  "vo": "4", "mu": "5", 
  "xa": "6", "ze": "7",
  "bi": "8", "so": "9"
}

lojban = input("Write a number in lojiban: ")

for i in range(0, len(lojban), 2):
  denary.append(lojbanDict[lojban[i:i+2]])

print("".join(denary))
