#Solution by @Pararcana
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
encryptor, answer = [], []
counter = 0

n = input("Input a number and word. ").split()

for _ in range(26):
  counter += int(n[0]) <= 26 and int(n[0])-1 or (int(n[0]) % len(alphabet)) - 1
  if counter >= len(alphabet):
    counter %= len(alphabet)
  encryptor.append(alphabet.pop(counter))
print("".join(encryptor[0:6]))

for i in range(len(n[1])):
  answer.append(encryptor[ord(n[1][i])-65])
  encryptor.append(encryptor.pop(0))
  
print("".join(answer))
