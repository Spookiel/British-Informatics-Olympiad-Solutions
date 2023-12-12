#Solution by @Pararcana
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
ring, answer = [], []
counter = 0

number, word = input("Input a number and word. ").split()
number, word = int(number), word.upper()

for _ in range(26):
  counter += (number % len(alphabet)) - 1
  if counter >= len(alphabet):
    counter %= len(alphabet)
  elif counter == -1:
    counter = len(alphabet) - 1
  ring.append(alphabet.pop(counter))
print("".join(ring[0:6]))

for i in range(len(word)):
  answer.append(ring[ord(word[i])-65])
  ring.append(ring.pop(0))
print("".join(answer))
