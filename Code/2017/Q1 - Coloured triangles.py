def solve(start):
    new = ""
    for i in range(1, len(start)):
        pair = start[i - 1:i + 1]
        if len(set(pair)) == 1:
            new += pair[0]
        else:
            new += d["".join(sorted(pair))]
    return new


start = input()

d = {"GR":"B", "BR":"G", "BG":"R"}

while len(start) > 1:
    start = solve(start)
print(start)

def b():
    string = "RRGBRGBB"
    starts = ["RR", "GB", "BG"]
    for start in starts:
        pos = 1
        while len(start) < 9:
            if start[-1] == string[pos]:
                start += start[-1]
            else:
                start += (set("RGB")-set(start[-1])-set(string[pos])).pop()
            pos += 1
        print(start)

#b()