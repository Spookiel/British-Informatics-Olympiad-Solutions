#Solution by @Pararcana
words = (
  "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
  "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", 
  "eighteen", "nineteen", "twenty", "twenty-one", "twenty-two", "twenty-three", 
  "twenty-four", "twenty-five", "twenty-six", "twenty-seven", "twenty-eight", "twenty-nine", "half"
)

hours = int(input("Hours: "))
minutes = int(input("Minutes: "))

half = "to" if minutes > 30 else "past"
if minutes > 30:
  hours += hours == 12 and -11 or 1
  minutes = 60 - minutes
special = minutes not in (15, 30, 45) and "minutes " or ""

if minutes == 0:
  print(f"{words[hours]} o'clock")
else:
  print(f"{words[minutes]} {special}{half} {words[hours]}")
