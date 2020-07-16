alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

let1, let2, n = input().split()
n = int(n)

let1 = alpha.index(let1)+1
let2 = alpha.index(let2)+1

for i in range(n-2):
    let1,let2 = let2, (let1+let2)%26

if n==1:
    print(alpha[let1-1])
else:

    print(alpha[let2-1])
""
def b():
    a = alpha.index("X")-alpha.index("F")
    print(alpha[a])
    c = (alpha.index("H")-alpha.index("Q"))%26
    print(alpha[c])

from numpy.linalg import matrix_power

def c(num):
    pass

#b) S, R

