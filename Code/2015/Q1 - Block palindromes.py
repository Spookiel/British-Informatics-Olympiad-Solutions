



s = input()

from itertools import combinations



def solve(s, partB=False):
    count = 0
    for splits in range(1,len(s)):
        for pos in combinations(range(1, len(s)), splits):
            got = []
            last = 0
            for i in pos:
                got.append(s[last:i])
                last = i
            got.append(s[last:])

            if got==got[::-1]:
                if partB:
                    print(got)
                count += 1
    return count

ans = solve(s)
print(ans)

def b():
    cstring = "AABCBAA"
    solve(cstring, partB=True)


# b() -> (A)(ABCBA)(A), (AA)(BCB)(AA), (A)(A)(BCB)(A)(A),(AA)(B)(C)(B)(AA),(A)(A)(B)(C)(B)(A)(A)

#c) The length of the block palindrome has to be even. The sum of the lengths of the palindrome can be represented as
# a sequence of even numbers, eg 2,4,2,2. Since any number of even numbers summed gives an even number, the length of
# has to be of an even length.
# ABABAB


def c():
    #Contains code used to verify and test assertions for part C
    for i in range(2,12):
        print(solve("AB"*i), i*2)
#c()



