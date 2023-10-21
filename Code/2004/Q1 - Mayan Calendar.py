from datetime import timedelta,date
baseDate = list(map(int,"13 20 7 16 3".split()))[::-1]
realDate = list(map(int, input("ENTER DATE: ").split()))[::-1]
janDate = date(2000, 1, 1)


def convert(baseDate, realDate):
    dayList = [20, 18, 20, 20] #Keeps track of how many kins in a uinal etc
    cumSum = [1, 20, 360, 7200, 144000] #Cumulative sum of the days in each part of the calender, eg 144000 days in a Baktun
    ansDate = [0, 0, 0, 0, 0] #Empty list to keep track of the new date

    for i in range(len(realDate)): #We're doing a subtraction, treating each element of a the calender as a digit so to speak
        if baseDate[i] > realDate[i]: #Keeps everything positive
            realDate[i+1] -= 1
            realDate[i] += dayList[i]
        ansDate[i] = realDate[i]-baseDate[i]


    totDays = sum([ansDate[i]*cumSum[i] for i in range(len(ansDate))]) #Works out the total number of days in our date difference
    finalDate = janDate+timedelta(days=totDays) #Uses Python's Datetime library to skip forward the correct number of days
    finalDate =str(finalDate).split("-")[::-1] #Gets date
    finalDate = [i if int(i) >= 10 else i[1:] for i in finalDate] #Formats date
    print(" ".join(finalDate))


convert(baseDate, realDate)

#b)13 20 7 17 14 , 13 20 8 16 9
""" Working for b)
febDate = date(2000,2,1)
print(febDate-janDate)
print(baseDate)
ans = [14,17,7,20,13]
convert(baseDate, ans)
aheadJanDate = date(2001,1,1)
print(aheadJanDate-janDate)
#366 day difference - Increase greedily, third number by one, first number by six  (Looking at the cumulative sum)
ans = [9,16,8,20,13] #Make sure to reverse
convert(baseDate, ans)"""

#c) 144000 days in a baktun, 20 baktuns in a cycle - 2,880,000 days in a cycle.  Thursday
""" Date that the current cycle ends on is 12 10 4772
endDate = date(4772, 10, 12)
print(endDate.weekday()) #0 is Monday, 6 is Sunday
#Gives answer as 3 or Thursday"""

""" Analysis
Solution scores 29/29
This solution uses Python's Datetime library to get full credit very easily.
You don't even have to know the library off by heart - You can look at the docs during the exam.
This is a library that is definitely worth keeping in mind as it is extremely powerful and easy to use.


"""
