#Solution made by @Pararcana
num = "{:04d}".format(int(input("Please input a number: ")))
ans = []
roman = [
["M", ""],
["C", "D", "M", ""],
["X", "L", "C", ""],
["I", "V", "X", ""]
]
format = [[-1], [0], [0,0], [0,0,0], [0,1], [1], [1,0], [1,0,0], [1,0,0,0], [0,2]]
for i, n in enumerate(num):
    for j in range(len(format[int(n)])):
        ans.append(roman[i][format[int(n)][j]])
    
return "".join(ans)
