

s1,s2 = input().split()




def check(string):
    #print(string)
    if len(string)==1:
        return True
    if len(string)==2:
        if string[0] > string[1]:
            return True
        return False
    for pos in range(1,len(string)):
        left, right = string[:pos], string[pos:]
        #print(left, right)

        #if reverse of left and right are both pats

        if check(left[::-1]) and check(right[::-1]):
            got = max(right)
            #print(got, right, left, string, "HERE")
            flag = True
            for char in left:
                if char <= got:
                    flag = False
            if flag:
                return True
    return False

for string in [s1, s2, s1+s2]:
    ans = check(string)

    if not ans:
        print("NO")
    else:
        print("YES")