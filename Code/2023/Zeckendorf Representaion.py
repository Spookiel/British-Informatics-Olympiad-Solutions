#Solution by @Pararcana
fib = [1, 2]
ans = []
total = 0

while fib[-1] < 1000000:
  fib.append(fib[-1] + fib[-2])
fib.reverse()

num = int(input("Number: "))

for i in fib:
  if i + total <= num:
    total += i
    ans.append(i)

print(ans)
