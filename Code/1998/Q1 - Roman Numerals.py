#Solution made by @Pararcana
roman = []
num = 5000
total = 0
numerals = {1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
}
denary = int(input("Please input a number: "))

for i in range(1, 8):
  num = num / (i % 2 == 0 and 2 or 5)
  for _ in range(3):
    if num + total <= denary:
      roman.append(numerals[int(num)])
      total += num
    elif (i%2==0 and num*4/5 or num*9/10) + total <= denary:
      roman.append(numerals[int(i%2==0 and num/(i%2!=0 and 2 or 5) or num/10)])
      roman.append(numerals[int(num)])
      total += i%2==0 and num*4/5 or num*9/10

print("".join(roman))
