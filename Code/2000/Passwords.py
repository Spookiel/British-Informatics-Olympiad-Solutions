#Made by @Catatria
password = str(input("Input a password. ")) # Prompts user for input that will be checked

# Sets variables that I use later
count = 0
round = 1
length = len(password)
length2 = int(length/2)

# Performs checks to see if the input is valid
if length <= 0:
  print("\nPassword too short; minimum 1 character.\n")
  exit()
elif length == 1: # I cut corners here, if the password is one character long there cannot be any repeated characters; therefore, the password is valid
  print("\nAccepted\n")
  exit()
elif length >= 11:
  print("\nPassword too long; maximum 10 characters.\n")
  exit()
elif password.isupper() == False:
  print("\nAll characters must be uppercase.\n")
  exit()

# Main block of code that checks if a password meets the criteria for approval
while True: # Infinite loop
  if password[count: count + round] != password[count + round: count + round * 2]: # Checks if there is a repeating pattern in the code, the check widens from one digit to 4 depending on count.
    count += 1 # Count increments
    if count + 1 == length: # Checks if I have checked for repeats until the last character of the password
      if length2 == round: # Checks if the amount of characters that I am checking for repeats has reached half or more of the password, if so, the password is accepted.
        print("\nAccepted\n")
        exit() # Program accepts and terminates as requested
      count = 0 # Count is reset, ready for checks with a longer string of characters
      round += 1 # Round increments
  else:
    print("\nRejected\n")
    exit() # Program rejects and terminates as requested
