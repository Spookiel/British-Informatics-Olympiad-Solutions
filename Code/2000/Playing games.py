#Solution made by @Catatria
# If the sides on your dice is 8, expect to wait ~5 seconds
# For the last test, the answer it gives you is different to the answers on the markscheme; however, it is still correct
# Proof: shorturl.at/CFT14 or https://docs.google.com/spreadsheets/d/1_kKzVkg_O4bm8mu5jpZ7_C3qjI-kHdi7pLFs1WH2P6w/edit?usp=sharing
def check(sides, check1, info1, info2, sample1, sample2): # Creates a function called check
  global finish, final1, final2 # Allows these variables to be used in global scope
  for m in range(sides):
    for n in range(sides):
      check2.append(sample1[m] + sample2[n]) # Appends every possible outcome of dice
  check2.sort() # Sorts it
  if check1 == check2: # Checks if both dice are fair
    if sample1 != info1 and sample2 != info2: 
      if sample1 != info2 and sample2 != info1: # Checks if the dice are repeats
        finish = True # Makes finish true so it will print out the outcome later
        final1 = sample1.copy()
        final2 = sample2.copy() # If they aren't, the dice are saved to be printed out later
  check2.clear() # Clears check2 for the next use


def middle(list1, list2, list3, list4, choice): # Creates a function called middle which finds a pair of numbers that adds to the pair of numbers inputted
  x = int(list1)
  y = int(list2)
  z = x + y # Finds sum of pair
  for i in range(int(z/2)):
    d = x + i # Finds numbers that equal the sum of that pair by adding and subtracting consecutive numbers
    f = y - i
    k = int((d+f)/2) # Finds average that may be used if sides of dice is odd
    if choice == 0: # Appends solutions to whichever list I picked based on a variable called choice
      middleList1.append([d,f])
    elif choice == 1:
      middleList1.append([d,k,f])
    elif choice == 2:
      middleList3.append([d,f])
    elif choice == 3:
      middleList3.append([d,k,f])
    elif choice == 4:
      middleList5.append([d,f])
  a = int(list3)
  b = int(list4)
  c = a + b
  for j in range(int(c/2)):
    g = a + j
    h = b - j
    l = int((g+h)/2) # Same thing over here
    if choice == 0:
      middleList2.append([g,h])
    elif choice == 1:
      middleList2.append([g,l,h])
    elif choice == 2:
      middleList4.append([g,h])
    elif choice == 3:
      middleList4.append([g,l,h])
    elif choice == 4:
      middleList6.append([g,h])


def valid(example, sides, dice): # Creates a function called valid
  for i in range(len(example)):
    if int(example[i]) < 1 or int(example[i]) > 8: # Checks if input is valid
      print("\nError: Number on (one of the sides on) dice is either below one or above eight.\n")
      exit()
  if dice == True:
    if len(example) != sides: # Also checks if input is valid
      print("\nError: Number of sides on dice and sides specified do not match.\n")
      exit()


sides = int(input("Number of sides: ")) # Prompts user for input
valid([sides], sides, False) # Checks input
dice1 = input("\nDice 1: ") # Prompts user for input
info1 = dice1.split(" ") # Turns input into list
valid(info1, sides, True) # Checks input
dice2 = input("Dice 2: ") # Prompts user for input
info2 = dice2.split(" ") # Turns input into list
valid(info2, sides, True) # Checks input

smallSolutions, bigSolutions, check1, check2, possibilities, test1, test2, test3, test4, test5, test6 = [], [], [], [], [], [], [], [], [], [], []
middleList1, middleList2, middleList3, middleList4, middleList5, middleList6 = [], [], [], [], [], []
finish = False # Creates and assigns a lot of variables values

for i in range(sides*2): # Turns all items in the lists from strings to integers
  if i < sides:
    info1[i] = int(info1[i])
  else:
    info2[i-sides] = int(info2[i-sides])
    
info1.sort()
info2.sort() # Sorts the lists

small = int(info1[0]) + int(info2[0]) # Finds the sum of the smallest numbers
big = int(info1[sides-1]) + int(info2[sides-1]) # Finds the sum of the largest numbers
for i in range(int(small/2)):
  x = i + 1
  y = small - (i + 1)
  smallSolutions.append([x,y]) # Finds a pair of numbers that add up to the same as the other pair
for i in range(int(big/2)):
  x = i + 1
  y = big - (i + 1)
  bigSolutions.append([x,y]) # Finds a pair of numbers that add up to the same as the other pair
for i in range(sides):
  for j in range(sides):
    check1.append(info1[i]+info2[j]) # Finds all possible combinations of dice rolls
    check1.sort() # Sorts it
for x in range(len(smallSolutions)):
  for y in range(len(bigSolutions)):
      possibilities.append([smallSolutions[x][0],bigSolutions[y][0]])
      possibilities.append([smallSolutions[x][1],bigSolutions[y][1]]) # Appends these pairs to a list called possibilities
for i in range(len(possibilities)):
  possibilities[i].sort() # Sorts each list within possibilities

if sides == 1:
  for i in range(int(small/2)):
    x = i + 1
    y = small - (i + 1) # Finds a pair of numbers which add up to the pair inputted
    check(sides, check1, info1, info2, [x], [y]) # Checks it
else:
  for e in range(int(len(possibilities)/2)):
    if sides == 2: # If sides is 2, it checks possibilities if the answer is correct
      check(sides, check1, info1, info2, [possibilities[e*2][0], possibilities[e*2][1]], [possibilities[(e*2)+1][0], possibilities[(e*2)+1][1]])
    elif sides == 3:
      middle1 = int((possibilities[e*2][0] + possibilities[e*2][1])/2)
      middle2 = int((possibilities[(e*2)+1][0] + possibilities[(e*2)+1][1])/2)
      test1 = [possibilities[e*2][0], middle1, possibilities[e*2][1]]
      test2 = [possibilities[(e*2)+1][0], middle2, possibilities[(e*2)+1][1]] # Appends a middle (average of both sides) to the dice
      test1.sort()
      test2.sort() # Sorts it
      check(sides, check1, info1, info2, test1, test2) # Checks it
    elif sides != 5: # Finds a pair of numbers that add up to the pair of numbers surrounding it
      middle(possibilities[e*2][0], possibilities[e*2][1], possibilities[(e*2)+1][0], possibilities[(e*2)+1][1], 0)
    elif sides == 5: # Same thing but I changed the variable choice so it will also append the average to get an extra side on the dice
      middle(possibilities[e*2][0], possibilities[e*2][1], possibilities[(e*2)+1][0], possibilities[(e*2)+1][1], 1)
    for zi in range(len(middleList1)):
      for yj in range(len(middleList2)):
        if sides != 5:
          test1.append([possibilities[e*2][0], middleList1[zi][0], middleList1[zi][1], possibilities[e*2][1]])
          test2.append([possibilities[(e*2)+1][0], middleList2[yj][0], middleList2[yj][1], possibilities[(e*2)+1][1]])
        else: # Appends to a new variable called test
          test1.append([int(possibilities[e*2][0]), int(middleList1[zi][0]), int(middleList1[zi][1]), int(middleList1[zi][2]), int(possibilities[e*2][1])])
          test2.append([int(possibilities[(e*2)+1][0]), int(middleList2[yj][0]), int(middleList2[yj][1]), int(middleList2[yj][2]), int(possibilities[(e*2)+1][1])])
        test1[0].sort()
        test2[0].sort()
        if sides == 4 or sides == 5:
          check(sides, check1, info1, info2, test1[0], test2[0]) # Checks solution if sides is 4 or 5
        else:
          if sides != 7: # Finds another pair of numbers
            middle(test1[0][1], test1[0][2], test2[0][1], test2[0][2], 2)
          elif sides == 7: # Finds 3 numbers
            middle(test1[0][1], test1[0][2], test2[0][1], test2[0][2], 3)
          for xi in range(len(middleList3)):
            for wj in range(len(middleList4)):
              for k in range(4):
                test3.append(test1[0][k])
                test4.append(test2[0][k])
              test3.append(middleList3[xi][0])
              test3.append(middleList3[xi][1])
              test4.append(middleList4[wj][0])
              test4.append(middleList4[wj][1]) # Appends the results to a new list
              if sides == 7:
                test3.append(middleList3[xi][2])
                test4.append(middleList4[wj][2]) # Appends the extra side if the sides is 7
              test3.sort()
              test4.sort() # Sorts the lists
              if sides == 6 or sides == 7: # Checks the solutions if sides are 6 and 7
                check(sides, check1, info1, info2, test3, test4)
              else:
                middle(test3[2], test3[3], test4[2], test4[3], 4) # Finds another pair
                for vi in range(len(middleList5)):
                  for uj in range(len(middleList6)):
                    for l in range(6):
                      test5.append(test3[l])
                      test6.append(test4[l]) 
                    test5.append(middleList5[vi][0])
                    test5.append(middleList5[vi][1])
                    test6.append(middleList6[uj][0])
                    test6.append(middleList6[uj][1]) # Appends them to a new list
                    test5.sort()
                    test6.sort()
                    check(sides, check1, info1, info2, test5, test6) # Checks it
                    test5.clear()
                    test6.clear()
                middleList5.clear()
                middleList6.clear()
              test3.clear()
              test4.clear() 
          middleList3.clear()
          middleList4.clear()
        test1.clear()
        test2.clear()
    middleList1.clear()
    middleList2.clear() # Resets the lists to be used again
if finish: # Checks if it found a solution
  for i in range(sides):
    final1[i] = str(final1[i])
    final2[i] = str(final2[i]) # Turns items in list from int to str for concatenation
  dice1Solution = " ".join(final1)
  dice2Solution = " ".join(final2) # Makes format nice
  print("\nDice 1: " + dice1Solution)
  print("Dice 2: " + dice2Solution) # Prints out solution if it did
else:
  print("\nImpossible") # Else, prints impossible
