#Solution by @Pararcana
password = input("Input a password: ").upper()
repeat = False

for i in range(len(password)):
  for j in range(1, int(len(password)/2) + 1):
    if i+2*j <= len(password) and password[i:i+j] == password[i+j:i+2*j]:
      repeat = True

print(repeat and "Rejected" or "Accepted")
