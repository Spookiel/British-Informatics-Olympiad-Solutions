#Solution made by @Catatria
#if the sides on your dice is 8, expect to wait ~15 seconds
# for the last test, the answer it gives you is different to the answers on the markscheme, however, it is still correct
# proof: shorturl.at/CFT14

sides = int(input("Number of sides: "))
if sides < 1 or sides > 8:
  print("\nError: Number of sides on dice is either below one or above eight.\n")
  exit()


dice1 = input("\nDice 1: ")
info1 = dice1.split(" ")
if len(info1) != sides:
  print("\nError: Number of sides on dice 1 and sides specified do not match.\n")
  exit()
for i in range(len(info1)):
  if int(info1[i]) < 1 or int(info1[i]) > 8:
    print("\nError: Number on one of the sides on dice 1 is either below one or above eight\n")
    exit()


dice2 = input("Dice 2: ")
info2 = dice2.split(" ")
if len(info2) != sides:
  print("\nError: Number of sides on dice 2 and sides specified do not match.\n")
  exit()
for i in range(len(info1)):
  if int(info2[i]) < 1 or int(info2[i]) > 8:
    print("\nError: Number on one of the sides on dice 2 is either below one or above eight.\n")
    exit()


finish = False
smallSolutions = []
bigSolutions = []
solutions = []
removeSmall = []
removeBig = []
remove = []
check1 = []
check2 = []
numberStorage = []
possibilities = []
middleList1 = []
middleList2 = []
middleList3 = []
middleList4 = []
middleList5 = []
middleList6 = []
test1 = []
test2 = []
test3 = []
test4 = []
test5 = []
test6 = []


for i in range(sides*2):
  if i < sides:
    info1[i] = int(info1[i])
  else:
    info2[i-sides] = int(info2[i-sides])
    

info1.sort()
info2.sort()


if sides == 1:
  small = int(info1[0]) + int(info2[0])
  for i in range(int(small/2)):
    x = i + 1
    y = small - (i + 1)
    solutions.append([x,y])
  for i in range(len(solutions)):
    if solutions[i] == [info1[0],info2[0]]:
      remove.append(i)
  solutions.pop(remove[0])
  if len(solutions) != 0:
    print("\nDice 1: " + str(solutions[0][0]))
    print("Dice 2: " + str(solutions[0][1]))
  else:
    print("\nImpossible")

    
elif sides == 2:
  small = int(info1[0]) + int(info2[0])
  big = int(info1[sides-1]) + int(info2[sides-1])
  for i in range(int(small/2)):
    x = i + 1
    y = small - (i + 1)
    smallSolutions.append([x,y])
  for i in range(int(big/2)):
    x = i + 1
    y = big - (i + 1)
    bigSolutions.append([x,y])
  for i in range(len(smallSolutions)):
    if smallSolutions[i][0] == info1[0] and smallSolutions[i][1] == info2[0]:
      remove.append(i)
  if len(remove) == 0:
    print("\nImpossible")
  smallSolutions.pop(remove[0])
  remove.clear()  
  for i in range(len(bigSolutions)):
    if bigSolutions[i][0] == info1[1] and bigSolutions[i][1] == info2[1]:
      remove.append(i)
  bigSolutions.pop(remove[0])
  remove.clear()
  for i in range(2):
    for j in range(2):
      check1.append(info1[i]+info2[j])
      check1.sort()
  for x in range(len(smallSolutions)):
    for y in range(len(bigSolutions)):
      for i in range(2): # sides
        for j in range(2):
          check2.append(smallSolutions[x][i]+bigSolutions[y][j])
          check2.sort()
      if check1 == check2:
        numberStorage.append(x)
        numberStorage.append(i)
        numberStorage.append(y)
        numberStorage.append(j)
        finish = True
      else:
        check2.clear()
  if finish:
    diceStorage = numberStorage.copy()
    diceStorage[1] -= 1
    diceStorage[3] -= 1
    print("\nDice 1: " + str(smallSolutions[diceStorage[0]][(diceStorage[1])]) , str(bigSolutions[(diceStorage[2])][(diceStorage[3])]))
    print("Dice 2: " + str(smallSolutions[numberStorage[0]][numberStorage[1]]) , str(bigSolutions[numberStorage[2]][numberStorage[3]]))
  else:
    print("\nImpossible")

    
elif sides == 3:
  small = int(info1[0]) + int(info2[0])
  big = int(info1[sides-1]) + int(info2[sides-1])
  for i in range(int(small/2)):
    x = i + 1
    y = small - (i + 1)
    smallSolutions.append([x,y])
  for i in range(int(big/2)):
    x = i + 1
    y = big - (i + 1)
    bigSolutions.append([x,y])
  for i in range(3):
    for j in range(3):
      check1.append(info1[i]+info2[j])
      check1.sort()
  for x in range(len(smallSolutions)):
    for y in range(len(bigSolutions)):
        possibilities.append([smallSolutions[x][0],bigSolutions[y][0]])
        possibilities.append([smallSolutions[x][1],bigSolutions[y][1]])
  for x in range(len(smallSolutions)):
    for y in range(len(bigSolutions)):
        possibilities.append([smallSolutions[x][1],bigSolutions[y][0]])
        possibilities.append([smallSolutions[x][0],bigSolutions[y][1]])
  for i in range(len(possibilities)):
    possibilities[i].sort()
  for i in range(len(possibilities)):
    evenOdd = possibilities[i][0] + possibilities[i][1]
    if (evenOdd % 2) != 0:
      remove.append(i)
  remove.reverse()
  for i in range(len(remove)):
    possibilities.pop(remove[i])  
  for i in range(len(possibilities)):
    middle = possibilities[i][0] + possibilities[i][1]
    middle = int(middle/2)
    possibilities[i].insert(1, middle)
  for x in range(int(len(possibilities)/2)):
    for i in range(3):
      for j in range(3):
        check2.append(possibilities[x*2][i] + possibilities[(x*2)+1][j])
        check2.sort()
    if check1 == check2:
      if possibilities[x*2] == info1 and possibilities[(x*2)+1] == info2: 
        pass
      elif possibilities[x*2] != info2 and possibilities[(x*2)+1] != info1:
        finish = True
        numberStorage.append(x)
      else:
        check2.clear()
    else:
      check2.clear()
  if finish:
    x = int(numberStorage[0])
    print("\nDice 1: " + str(possibilities[x*2][0]), str(possibilities[x*2][1]), str(possibilities[x*2][2]))
    print("Dice 2: " + str(possibilities[(x*2)+1][0]), str(possibilities[(x*2)+1][1]), str(possibilities[(x*2)+1][2]))
  else:
    print("\nImpossible")

    

    
elif sides == 4:
  small = int(info1[0]) + int(info2[0])
  big = int(info1[sides-1]) + int(info2[sides-1])
  for i in range(int(small/2)):
    x = i + 1
    y = small - (i + 1)
    smallSolutions.append([x,y])
  for i in range(int(big/2)):
    x = i + 1
    y = big - (i + 1)
    bigSolutions.append([x,y])
  for i in range(4):
    for j in range(4):
      check1.append(info1[i]+info2[j])
      check1.sort()
  for x in range(len(smallSolutions)):
    for y in range(len(bigSolutions)):
        possibilities.append([smallSolutions[x][0],bigSolutions[y][0]])
        possibilities.append([smallSolutions[x][1],bigSolutions[y][1]])
  for x in range(len(smallSolutions)):
    for y in range(len(bigSolutions)):
        possibilities.append([smallSolutions[x][0],bigSolutions[y][0]])
        possibilities.append([smallSolutions[x][1],bigSolutions[y][1]])
  for i in range(len(possibilities)):
    possibilities[i].sort()
  for i in range(int(len(possibilities)/4)):
    x = int(possibilities[i*2][0])
    y = int(possibilities[i*2][1])
    z = x + y
    for j in range(int(z/2)):
      f = x + j
      u = y - j
      middleList1.append([f,u])
    a = int(possibilities[(i*2)+1][0])
    b = int(possibilities[(i*2)+1][1])
    c = a + b
    for j in range(int(c/2)):
      f = a + j
      u = b - j
      middleList2.append([f,u])
    for j in range(len(middleList1)):
      for k in range(len(middleList2)):
        test1.append([possibilities[i*2][0], middleList1[j][0], middleList1[j][1], possibilities[i*2][1]])
        test2.append([possibilities[(i*2)+1][0], middleList2[k][0], middleList2[k][1], possibilities[(i*2)+1][1]])
        for m in range(4):
          for n in range(4):
            check2.append(test1[0][m] + test2[0][n])
            check2.sort()
        if check1 == check2:
          if test1[0] == info1 and test2[0] == info2: 
            pass
          elif test1[0] != info2 and test2[0] != info1:
            finish = True
            numberStorage.append(test1[0])
            numberStorage.append(test2[0])
        check2.clear()
        test1.clear()
        test2.clear()
    middleList1.clear()
    middleList2.clear()
  if finish:
    print("\nDice 1: " + str(numberStorage[0][0]),str(numberStorage[0][1]),str(numberStorage[0][2]),str(numberStorage[0][3]))
    print("Dice 2: " + str(numberStorage[1][0]),str(numberStorage[1][1]),str(numberStorage[1][2]),str(numberStorage[1][3]))
  else:
    print("\nImpossible")


elif sides == 5:
  small = int(info1[0]) + int(info2[0])
  big = int(info1[sides-1]) + int(info2[sides-1])
  for i in range(int(small/2)):
    x = i + 1
    y = small - (i + 1)
    smallSolutions.append([x,y])
  for i in range(int(big/2)):
    x = i + 1
    y = big - (i + 1)
    bigSolutions.append([x,y])
  for i in range(5):
    for j in range(5):
      check1.append(info1[i]+info2[j])
      check1.sort()
  for x in range(len(smallSolutions)):
    for y in range(len(bigSolutions)):
        possibilities.append([smallSolutions[x][0],bigSolutions[y][0]])
        possibilities.append([smallSolutions[x][1],bigSolutions[y][1]])
  for x in range(len(smallSolutions)):
    for y in range(len(bigSolutions)):
        possibilities.append([smallSolutions[x][0],bigSolutions[y][0]])
        possibilities.append([smallSolutions[x][1],bigSolutions[y][1]])
  for i in range(len(possibilities)):
    possibilities[i].sort()
  for i in range(int(len(possibilities)/4)):

    x = int(possibilities[i*2][0])
    y = int(possibilities[i*2][1])
    z = x + y
    a = int(possibilities[(i*2)+1][0])
    b = int(possibilities[(i*2)+1][1])
    c = a + b
    p = (x+j) + (y-j)
    p = p/2
    q = (a+j) + (b-j)
    q = q/2
    if p.is_integer() == True and q.is_integer() == True:
      for j in range(int(z/2)):
        f = x + j
        u = y - j
        middle = f + u
        middle = int(middle/2)
        middleList1.append([f, middle, u])
      for j in range(int(c/2)):
        f = a + j
        u = b - j
        middle = f + u
        middle = int(middle/2)
        middleList2.append([f, middle, u])
      for j in range(len(middleList1)):
        for k in range(len(middleList2)):
          test1.append([int(possibilities[i*2][0]), int(middleList1[j][0]), int(middleList1[j][1]), int(middleList1[j][2]), int(possibilities[i*2][1])])
          test2.append([int(possibilities[(i*2)+1][0]), int(middleList2[k][0]), int(middleList2[k][1]), int(middleList2[k][2]), int(possibilities[(i*2)+1][1])])
          test1[0].sort()
          test2[0].sort()
          for m in range(5):
            for n in range(5):
              check2.append(test1[0][m] + test2[0][n])
              check2.sort()
          if check1 == check2:
            if test1[0] == info1 and test2[0] == info2: 
              pass
            elif test1[0] != info2 and test2[0] != info1:
              finish = True
              numberStorage.append(test1[0])
              numberStorage.append(test2[0])
          check2.clear()
          test1.clear()
          test2.clear()
      middleList1.clear()
      middleList2.clear()
  if finish:
    print("\nDice 1: " + str(numberStorage[0][0]),str(numberStorage[0][1]),str(numberStorage[0][2]),str(numberStorage[0][3]),str(numberStorage[0][4]))
    print("Dice 2: " + str(numberStorage[1][0]),str(numberStorage[1][1]),str(numberStorage[1][2]),str(numberStorage[1][3]), str(numberStorage[1][4]))
  else:
    print("\nImpossible")


elif sides == 6:
  small = int(info1[0]) + int(info2[0])
  big = int(info1[sides-1]) + int(info2[sides-1])
  for i in range(int(small/2)):
    x = i + 1
    y = small - (i + 1)
    smallSolutions.append([x,y])
  for i in range(int(big/2)):
    x = i + 1
    y = big - (i + 1)
    bigSolutions.append([x,y])
  for i in range(sides):
    for j in range(sides):
      check1.append(info1[i]+info2[j])
      check1.sort()
  for x in range(len(smallSolutions)):
    for y in range(len(bigSolutions)):
        possibilities.append([smallSolutions[x][0],bigSolutions[y][0]])
        possibilities.append([smallSolutions[x][1],bigSolutions[y][1]])
  for x in range(len(smallSolutions)):
    for y in range(len(bigSolutions)):
        possibilities.append([smallSolutions[x][1],bigSolutions[y][0]])
        possibilities.append([smallSolutions[x][0],bigSolutions[y][1]])
  for i in range(len(possibilities)):
    possibilities[i].sort()
  for e in range(int(len(possibilities)/4)):
    ax = int(possibilities[e*2][0])
    ay = int(possibilities[e*2][1])
    az = ax + ay
    for ai in range(int(az/2)):
      ad = ax + ai
      af = ay - ai
      middleList1.append([ad,af])
    aa = int(possibilities[(e*2)+1][0])
    ab = int(possibilities[(e*2)+1][1])
    ac = aa + ab
    for aj in range(int(ac/2)):
      ag = aa + aj
      ah = ab - aj
      middleList2.append([ag,ah])
    for zi in range(len(middleList1)):
      for yj in range(len(middleList2)):
        test1.append([possibilities[e*2][0], middleList1[zi][0], middleList1[zi][1], possibilities[e*2][1]])
        test2.append([possibilities[(e*2)+1][0], middleList2[yj][0], middleList2[yj][1], possibilities[(e*2)+1][1]])
        bx = int(test1[0][1])
        by = int(test1[0][2])
        bz = bx + by
        for bi in range(int(bz/2)):
          bd = bx + bi
          bf = by - bi
          middleList3.append([bd,bf])
        ba = int(test2[0][1])
        bb = int(test2[0][2])
        bc = ba + bb
        for bj in range(int(bc/2)):
          bg = ba + bj
          bh = bb - bj
          middleList4.append([bg,bh])
        for xi in range(len(middleList3)):
          for wj in range(len(middleList4)):
            for k in range(4):
              test3.append(test1[0][k])
            test3.insert(2, middleList3[xi][0])
            test3.insert(3, middleList3[xi][1])
            for l in range(4):
              test4.append(test2[0][l])
            test4.insert(2, middleList4[wj][0])
            test4.insert(3, middleList4[wj][1]) 
            test3.sort()
            test4.sort()
            for m in range(sides):
              for n in range(sides):
                check2.append(test3[m] + test4[n])
                check2.sort()
            if check1 == check2:
              if test3 == info1 and test4 == info2: 
                pass
              elif test3 != info2 and test4 != info1:
                finish = True
                final1 = test3.copy()
                final2 = test4.copy()
            check2.clear()
            test3.clear()
            test4.clear()    
        test1.clear()
        test2.clear()
        middleList3.clear()
        middleList4.clear()
    middleList1.clear()
    middleList2.clear()
  if finish:
    for i in range(sides):
      final1[i] = str(final1[i])
      final2[i] = str(final2[i])
    dice1Solution = " ".join(final1)
    dice2Solution = " ".join(final2)
    print("\nDice 1: " + dice1Solution)
    print("Dice 2: " + dice2Solution)
  else:
    print("\nImpossible")


elif sides == 7:
  small = int(info1[0]) + int(info2[0])
  big = int(info1[sides-1]) + int(info2[sides-1])
  for i in range(int(small/2)):
    x = i + 1
    y = small - (i + 1)
    smallSolutions.append([x,y])
  for i in range(int(big/2)):
    x = i + 1
    y = big - (i + 1)
    bigSolutions.append([x,y])
  for i in range(sides):
    for j in range(sides):
      check1.append(info1[i]+info2[j])
      check1.sort()
  for x in range(len(smallSolutions)):
    for y in range(len(bigSolutions)):
        possibilities.append([smallSolutions[x][0],bigSolutions[y][0]])
        possibilities.append([smallSolutions[x][1],bigSolutions[y][1]])
  for x in range(len(smallSolutions)):
    for y in range(len(bigSolutions)):
        possibilities.append([smallSolutions[x][1],bigSolutions[y][0]])
        possibilities.append([smallSolutions[x][0],bigSolutions[y][1]])
  for i in range(len(possibilities)):
    possibilities[i].sort()
  for e in range(int(len(possibilities)/4)):
    ax = int(possibilities[e*2][0])
    ay = int(possibilities[e*2][1])
    az = ax + ay
    for ai in range(int(az/2)):
      ad = ax + ai
      af = ay - ai
      middleList1.append([ad,af])
    aa = int(possibilities[(e*2)+1][0])
    ab = int(possibilities[(e*2)+1][1])
    ac = aa + ab
    for aj in range(int(ac/2)):
      ag = aa + aj
      ah = ab - aj
      middleList2.append([ag,ah])
    for zi in range(len(middleList1)):
      for yj in range(len(middleList2)):
        test1.append([possibilities[e*2][0], middleList1[zi][0], middleList1[zi][1], possibilities[e*2][1]])
        test2.append([possibilities[(e*2)+1][0], middleList2[yj][0], middleList2[yj][1], possibilities[(e*2)+1][1]])
        bx = int(test1[0][1])
        by = int(test1[0][2])
        bz = bx + by
        for bi in range(int(bz/2)):
          bd = bx + bi
          bf = by - bi
          bk = int((bd+bf)/2)
          middleList3.append([bd,bk,bf])
        ba = int(test2[0][1])
        bb = int(test2[0][2])
        bc = ba + bb
        for bj in range(int(bc/2)):
          bg = ba + bj
          bh = bb - bj
          bl = int((bg+bh)/2)
          middleList4.append([bg,bl,bh])
        for xi in range(len(middleList3)):
          for wj in range(len(middleList4)):
            for k in range(4):
              test3.append(test1[0][k])
            test3.insert(2, middleList3[xi][0])
            test3.insert(3, middleList3[xi][1])
            test3.insert(4, middleList3[xi][2])
            for l in range(4):
              test4.append(test2[0][l])
            test4.insert(2, middleList4[wj][0])
            test4.insert(3, middleList4[wj][1]) 
            test4.insert(4, middleList4[wj][2]) 
            test3.sort()
            test4.sort()
            for m in range(sides):
              for n in range(sides):
                check2.append(test3[m] + test4[n])
                check2.sort()
            if check1 == check2:
              if test3 == info1 and test4 == info2: 
                pass
              elif test3 != info2 and test4 != info1:
                finish = True
                final1 = test3.copy()
                final2 = test4.copy()
            check2.clear()
            test3.clear()
            test4.clear()    
        test1.clear()
        test2.clear()
        middleList3.clear()
        middleList4.clear()
    middleList1.clear()
    middleList2.clear()
  if finish:
    for i in range(sides):
      final1[i] = str(final1[i])
      final2[i] = str(final2[i])
    dice1Solution = " ".join(final1)
    dice2Solution = " ".join(final2)
    print("\nDice 1: " + dice1Solution)
    print("Dice 2: " + dice2Solution)
  else:
    print("\nImpossible")


elif sides == 8: # might improve this later
  small = int(info1[0]) + int(info2[0])
  big = int(info1[sides-1]) + int(info2[sides-1])
  for i in range(int(small/2)):
    x = i + 1
    y = small - (i + 1)
    smallSolutions.append([x,y])
  for i in range(int(big/2)):
    x = i + 1
    y = big - (i + 1)
    bigSolutions.append([x,y])
  for i in range(8):
    for j in range(8):
      check1.append(info1[i]+info2[j])
      check1.sort()
  for x in range(len(smallSolutions)):
    for y in range(len(bigSolutions)):
        possibilities.append([smallSolutions[x][0],bigSolutions[y][0]])
        possibilities.append([smallSolutions[x][1],bigSolutions[y][1]])
  for x in range(len(smallSolutions)):
    for y in range(len(bigSolutions)):
        possibilities.append([smallSolutions[x][1],bigSolutions[y][0]])
        possibilities.append([smallSolutions[x][0],bigSolutions[y][1]])
  for i in range(len(possibilities)):
    possibilities[i].sort()
  for i in range(int(len(possibilities)/4)):
    x = int(possibilities[i*2][0])
    y = int(possibilities[i*2][1])
    z = x + y
    for j in range(int(z/2)):
      f = x + j
      u = y - j
      middleList1.append([f,u])
    a = int(possibilities[(i*2)+1][0])
    b = int(possibilities[(i*2)+1][1])
    c = a + b
    for j in range(int(c/2)):
      f = a + j
      u = b - j
      middleList2.append([f,u])
    for j in range(len(middleList1)):
      for k in range(len(middleList2)):
        test1.append([possibilities[i*2][0], middleList1[j][0], middleList1[j][1], possibilities[i*2][1]])
        x = int(test1[0][1])
        y = int(test1[0][2])
        z = x + y
        for j in range(int(z/2)):
          f = x + j
          u = y - j
          middleList3.append([f,u])
        test2.append([possibilities[(i*2)+1][0], middleList2[k][0], middleList2[k][1], possibilities[(i*2)+1][1]])
        a = int(test2[0][1])
        b = int(test2[0][2])
        c = a + b
        for j in range(int(c/2)):
          f = a + j
          u = b - j
          middleList4.append([f,u])
        for j in range(len(middleList3)):
          for k in range(len(middleList4)):
            for i in range(4):
              test3.append(test1[0][i])
            test3.insert(2, middleList3[j][0])
            test3.insert(3, middleList3[j][1])
            for i in range(4):
              test4.append(test2[0][i])
            test4.insert(2, middleList4[k][0])
            test4.insert(3, middleList4[k][1])
            x = test3[2]
            y = test3[3]
            z = x + y
            for j in range(int(z/2)):
              f = x + j
              u = y - j
              middleList5.append([f,u])
            a = test4[2]
            b = test4[3]
            c = a + b
            for j in range(int(c/2)):
              f = a + j
              u = b - j
              middleList6.append([f,u])
            for j in range(len(middleList5)):
              for k in range(len(middleList6)):
                for i in range(6):
                  test5.append(test3[i])
                test5.insert(3, middleList5[j][0])
                test5.insert(4, middleList5[j][1])
                for i in range(6):
                  test6.append(test4[i])
                test6.insert(3, middleList6[k][0])
                test6.insert(4, middleList6[k][1])
                test5.sort()
                test6.sort()
                for m in range(8):
                  for n in range(8):
                    check2.append(test5[m] + test6[n])
                    check2.sort()
                if check1 == check2:
                  if test5 == info1 and test6 == info2: 
                    pass
                  elif test5 != info2 and test6 != info1:
                    finish = True
                    final1 = test5.copy()
                    final2 = test6.copy()
                    final1.sort()
                    final2.sort()
                check2.clear()   
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
    middleList2.clear()
  if finish:
    for i in range(sides):
      final1[i] = str(final1[i])
      final2[i] = str(final2[i])
    dice1Solution = " ".join(final1)
    dice2Solution = " ".join(final2)
    print("\nDice 1: " + dice1Solution)
    print("Dice 2: " + dice2Solution)
  else:
    print("\nImpossible")
