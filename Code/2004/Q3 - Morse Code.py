dic = {"a":	".-", "h": "....", "o": "---", "v": "...-",
    "b":"-...",	"i": "..",	"p": ".--.", "w": ".--",
    "c":"-.-.",	"j": ".---", "q": "--.-", "x": "-..-",
    "d":"-..", "k": "-.-", "r": ".-.", "y": "-.--",
    "e":".", "l": ".-..", "s": "...", "z": "--..",
    "f":"..-.", "m": "--", "t": "-",
    "g":"--.", "n": "-.", "u": "..-"}

alpha = "abcdefghijklmnopqrstuvwxyz"
word = input()
length = len(word)
import time
start = time.time()


def to_morse(data):
    ans = ""
    for i in data:
        ans += dic[i]
    return ans


def solve(cur, left):
    if left*4 < len(cur):
        return 0
    if left==0:
        if len(cur)==0:
            return 1
        else:
            return 0
    total = 0
    for possible in range(1,5):
        if possible <= len(cur):
            check = cur[:possible]
            if check in dic.values():
                total += solve(cur[possible:], left-1)
    return total


morseWord = to_morse(word)
#print(morseWord)


print(solve(morseWord, length))
print("EXECUTED IN", time.time()-start, "SECONDS")
#3b) 13,170

def solve_partB(morse):
    total = 0
    for l in range(20):
        total += solve(morse, l)
    return total
#print(solve_partB("-..-----."))

#3c) 130 - 5 bits for each letter in binary, 2**5 > 26


"""Analysis - Scores 32/34

This is a problem that can be solved with recursion. The maximum length of a letter in morse code is 4 letters long
Therefore, if we consider every prefix of our word up to four letters, calling this prefix string P.
If P is a valid encoding of a letter, then we can call our function solve again, this time with everything from len(P)
to the end (using zero indexing).

The other thing we need to keep track of is the number of letters we have left to use, at the start, this is the number of
letters in the english word that we are given as an input, and every time we call our function solve(), we pass the current
string, which starts as the full morse encoding of a word, and the number of letters that we can use. Therefore, every time we call
the function from itself, we decrease the number of letters left by one.

It remains to think about what the base cases are.
Well, if we have no letters left to use, and we're working on a string which has a length greater than zero, then we must return 0,
as there are no valid encodings of that word.
If we have no letters left to use, and the length of the current string is zero, then it is a valid string and we return 1

More mathematically, the recurrence relation is     solve(word, letters) = {1 if len(word)==0 and letters==0,
                                                                            0 if letters > 0 and len(word)==0,
                                                                            sum(solve(word[i:], letters-1), for all valid prefixes of lengths 1...4 (inclusive)}
                                                                            
                                                                            
It suffices to not make any improvements for this to run in time, as the maximum length is only 10 letters.




"""