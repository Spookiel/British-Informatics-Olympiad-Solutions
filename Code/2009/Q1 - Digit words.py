# Code by @Pararcana
digitWords = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN"]
word = input("Enter a word: ").upper()

for digit in digitWords:
  wordFilter = [v for v in word if v in digit]
  order = []
  counter = 0
  
  for v in digit:
    try:
      first = wordFilter.index(v)
      order.append(first + counter)
      wordFilter = [v for i, v in enumerate(wordFilter) if i > first]
      counter += first + 1
    except ValueError:
      break  
      
  if sorted(order) == order and len(order) == len(digit):
    print(digitWords.index(digit) + 1)
    exit()
print("NO")


def b():
    import re
    # No. of ways of making two from subsequences

    prefix = [[0,0,0]]*9
    targ = "TWOTWOTWO"
    from itertools import permutations,combinations
    counter = 0
    for perm in combinations(targ, 3):
        if "".join(perm)=="TWO":
            counter += 1
    print(counter)


#b) b() -> 10

#c)


def c():
    lets = set("".join(words[:5]))
    print(lets)
    lets = set("".join(words))
    print(lets)


c()

#12,16
