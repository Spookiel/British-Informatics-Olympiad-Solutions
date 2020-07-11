


import re

pattern = input()
patternCopy = pattern[:]
pattern = pattern.replace("d", "\d")
pattern = pattern.replace("u", "\d")
pattern = pattern.replace("x", "\d")

def solve(pattern,pattern2, password):

    if re.match(r""+pattern, password):
        print("MATCHES")
        length = len(password)

for i in range(2):
    code = input()
    solve(pattern, patternCopy, code)