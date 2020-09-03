


n = int(input())


#12345
#12421



#9634127
#9634369


#12945
#13031

#123456
#124421


#456123
#456654


def brute(n):
    while True:
        n += 1
        if str(n)==str(n)[::-1]:
            return n


def solve(n):
    if n==9:
        return 11
    if n < 10:
        return n+1
    sn = str(n)
    if len(sn)%2==0:
        fhalf = int("".join(sn[:len(sn)//2]))
        shalf = int("".join(sn[len(sn)//2:]))
        flag = False
        if sn==sn[::-1]:
            fhalf += 1
            flag = True
        if len(set(sn)) == 1 and sn[0] == "9":
            return "1" + ("0" * (len(sn) - 1)) + "1"
        if str(fhalf)[::-1] > str(shalf):

            return str(fhalf)+str(fhalf)[::-1]
        fhalf += 1 if not flag else 0
        return str(fhalf)+str(fhalf)[::-1]
    else:
        #991
        #1001

        #891
        #909
        #123
        fhalf = int("".join(sn[:len(sn)//2]))
        shalf = int("".join(sn[(len(sn)+1)//2:]))
        mid = int(sn[len(sn)//2])
        #print(fhalf, shalf, mid)
        if mid < 9:
            #print("HERE")
            mid += 1 if str(fhalf)[::-1] <= str(shalf) else 0
            return str(fhalf)+str(mid)+str(fhalf)[::-1]
        else:
            if len(set(sn))==1 and sn[0]=="9":
                return "1" + ("0" * (len(sn) - 1)) + "1"
            fhalf += 1
            mid = "0"

            return str(fhalf)+mid+str(fhalf)[::-1]





ans = solve(n)
print(ans)

def b():
    ma = 0
    last = 1
    cur = 2
    while True:

        if (dif := cur-last) > ma:
            print(cur, last, dif, len(str(cur)))
            ma = dif
        last = int(cur)
        cur = int(solve(cur))
        if len(str(cur)) > 20:
            break
#b()

#b() -> 11,000,000,000

def c_helper(n,got):
    gotset = set(got)
    low = 0
    high = len(got)-1
    while True:
        mid = (high+low)//2
        if mid==low:
            break
        if got[mid] < n:
            low = mid
        else:
            high = mid-1
    n -= got[low]

    if n in gotset:
        print(n, got[low], n+got[low], "HERE")
        return True
    print("FAILED", n+got[low], got[low], got[high])
    return False


def c():
    got = []
    cur = 1
    while cur < 100000:
        got.append(cur)
        cur = int(solve(cur))

    for i in range(1,100):
        ans = c_helper(i, got)

    #10,000
#c()