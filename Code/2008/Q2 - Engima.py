



r1 = {0:0, 1:3, 2:1,3:2} # ---> [2,0,1,3]
r2 = {0:0, 1:2, 2:1,3:3}
reflector = {0:3, 3:0, 1:2, 2:1}
def rotate(wheel):
    for k,v in list(wheel.items()):
        wheel[k-1] = (v-1)%4

    for k,v in list(wheel.items()):
        if k < 0:
            wheel[k%4] = v
            del wheel[k]
    return wheel

def traceRight(r1, r2, reflector, letter):
    letter = ord(letter)-65

    npos = r1[letter]
    npos = r2[npos]
    npos = reflector[npos]
    return npos



def traceLeft(r1, r2, pos):

    for k,v in r2.items():
        if v==pos:
            pos = k
            break

    for k,v in r1.items():
        if v==pos:
            pos = k
            break
    return pos


def traceFull(r1,r2,reflector, letter):
    rhsPos = traceRight(r1, r2, reflector, letter)
    fletter = traceLeft(r1, r2, rhsPos)
    return chr(fletter+65)

print(traceFull(r1, r2, reflector, "D"))



n = int(input())

message = input()

fspins = n%4
sspins = (n//4)%4
for i in range(fspins):
    r1 = rotate(r1)

for i in range(sspins):
    r2 = rotate(r2)

ans = ""
for letter in message:
    ans += traceFull(r1,r2,reflector, letter)
    r1 = rotate(r1)
    if (len(ans)+fspins)%4==0:
        r2 = rotate(r2)
print(ans)

