#Solution by @Pararcana
aIncre, bIncre = (int(x) + 60 for x in input("Enter two numbers: ").split())
a, b = aIncre, bIncre

def minutesToHours(min):
  return [(min // 60) % 24, min % 60]

while minutesToHours(a) != minutesToHours(b):
  a += aIncre
  b += bIncre

hours, minutes = minutesToHours(a)
print("{:02d}".format(hours)+":"+"{:02d}".format(minutes))

#Rest by Spookiel
def b():
    for i in range(20):
        print(solve(0, i,debug=True), i)

# b) -> 0, 8, 9, 16, 18



def c():
    best = 0
    for i in range(400):
        print(i)
        for j in range(400):
            useless, hours = solve(i,j, debug=True)
            if hours > best:
                best = hours
    print(best, "PART C")

#c) 1440 hours
