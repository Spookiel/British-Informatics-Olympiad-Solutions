


n = int(input())

terms = [input() for i in range(n)]

got = set()

for i in terms:
    for j in i:
        got.add(j)

print(got)