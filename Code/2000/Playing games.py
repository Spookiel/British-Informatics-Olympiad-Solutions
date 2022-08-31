#Solution made by @Catatria
# If sides is 8, expect to wait 5+ seconds
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
        for i in range(sides):
          final1[i] = str(final1[i])
          final2[i] = str(final2[i]) # Turns items in list from int to str for concatenation
        dice1Solution = " ".join(final1)
        dice2Solution = " ".join(final2) # Makes format nice
        print("\nDice 1: " + dice1Solution)
        print("Dice 2: " + dice2Solution + "\n") # Prints out solution if it did
        exit()
  check2.clear() # Clears check2 for the next use


def middle(list1, list2, list3, list4, middle1, middle2, choice): # Creates a function called middle which finds a pair of numbers that adds to the pair of numbers inputted
  x = int(list1)
  y = int(list2)
  z = x + y # Finds sum of pair
  for i in range(int(z/2)):
    d = x + i # Finds numbers that equal the sum of that pair by adding and subtracting consecutive numbers
    f = y - i
    k = int((d+f)/2) # Finds average that may be used if sides of dice is odd
    if sides % 2 == 0: # Checks if sides is even
      middle1.append([d,f])
    else:
      middle1.append([d,k,f])
  a = int(list3)
  b = int(list4)
  c = a + b
  for j in range(int(c/2)):
    g = a + j
    h = b - j
    l = int((g+h)/2) # Same thing over here
    if sides % 2 == 0:
      if choice == 0:
        middle2.append([g,h])
      else:
        middle2.append([g,h+1])
    else:
      middle2.append([g,l,h])


def valid(example, sides, dice): # Creates a function called valid
  for i in range(len(example)):
    if int(example[i]) < 1 or int(example[i]) > 8: # Checks if input is valid
      print("\nError: Number on (one of the sides on) dice is either below one or above eight.\n")
      exit()
  if dice == True:
    if len(example) != sides: # Also checks if input is valid
      print("\nError: Number of sides on dice and sides specified do not match.\n")
      exit()


def reset2(list1, list2):
  list1.clear()
  list2.clear()


def sort2(list1, list2):
  list1.sort()
  list2.sort()


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
    
sort2(info1, info2) # Sorts the lists

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

for iter in range(2):
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
        sort2(test1, test2) # Sorts it
        check(sides, check1, info1, info2, test1, test2) # Checks it
      else:
        middle(possibilities[e*2][0], possibilities[e*2][1], possibilities[(e*2)+1][0], possibilities[(e*2)+1][1], middleList1, middleList2, 0)
        for zi in range(len(middleList1)):
          for yj in range(len(middleList2)):
            if sides != 5:
              test1.append([possibilities[e*2][0], middleList1[zi][0], middleList1[zi][1], possibilities[e*2][1]])
              test2.append([possibilities[(e*2)+1][0], middleList2[yj][0], middleList2[yj][1], possibilities[(e*2)+1][1]])
            else: # Appends to a new variable called test
              test1.append([int(possibilities[e*2][0]), int(middleList1[zi][0]), int(middleList1[zi][1]), int(middleList1[zi][2]), int(possibilities[e*2][1])])
              test2.append([int(possibilities[(e*2)+1][0]), int(middleList2[yj][0]), int(middleList2[yj][1]), int(middleList2[yj][2]), int(possibilities[(e*2)+1][1])])
            sort2(test1[0], test2[0])
            if sides == 4 or sides == 5:
              check(sides, check1, info1, info2, test1[0], test2[0]) # Checks solution if sides is 4 or 5
            else:
              middle(test1[0][1], test1[0][2], test2[0][1], test2[0][2], middleList3, middleList4, iter)
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
                  sort2(test3, test4) # Sorts the lists
                  if sides == 6 or sides == 7: # Checks the solutions if sides are 6 and 7
                    check(sides, check1, info1, info2, test3, test4)
                  else:
                    middle(test3[2], test3[3], test4[2], test4[3], middleList5, middleList6, 0) # Finds another pair
                    for vi in range(len(middleList5)):
                      for uj in range(len(middleList6)):
                        for l in range(6):
                          test5.append(test3[l])
                          test6.append(test4[l]) 
                        test5.append(middleList5[vi][0])
                        test5.append(middleList5[vi][1])
                        test6.append(middleList6[uj][0])
                        test6.append(middleList6[uj][1]) # Appends them to a new list
                        sort2(test5, test6)
                        check(sides, check1, info1, info2, test5, test6) # Checks it
                        reset2(test5, test6)
                    reset2(middleList5, middleList6)
                  reset2(test3, test4)
              reset2(middleList3, middleList4)
            reset2(test1, test2)
        reset2(middleList1, middleList2) # Resets the lists to be used again
if not finish:
  print("\nImpossible\n")
  exit()
