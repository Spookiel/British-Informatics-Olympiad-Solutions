


units = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 0:""}
teens = {11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen"}
tens = {10:"Ten", 20:"Twenty", 30:"Half", 40:"Twenty", 50:"Ten", 15:"Quarter", 45:"Quarter", 0: ""}
hour = int(input())
minute = int(input())


fbit = ""
if minute == 0:
    pass
elif 0 < minute <= 30:

    if 10 < minute < 20:
        fbit = teens[minute]+" minutes" if minute != 15 else "Quarter"
    else:
        fbit = tens[(minute//10)*10]
        if minute%10 != 0 and minute > 10:
            fbit += "-"
        fbit += units[minute%10].lower()

        if minute not in [15,30]:
            fbit += " minutes" if minute != 1 else " minute"
    fbit += " past"
else:
    hour += 1
    hour %= 12
    if hour == 0:
        hour = 12
    minute = 60-minute
    if 10 < minute < 20:
        fbit = teens[minute]+" minutes" if minute != 15 else "Quarter"
    else:
        fbit = tens[(minute//10)*10]
        if minute%10 != 0 and minute > 10:
            fbit += "-"
        fbit += units[minute%10].lower()
        if minute not in [15,30]:
            fbit += " minutes" if minute != 1 else " minute"
    fbit += " to"



if minute!= 0:
    if hour < 10:
        fbit += " "+ units[hour].lower()
    elif hour == 10:
        fbit += " ten"
    else:
        fbit += " "+ teens[hour].lower()
else:
    if hour < 10:
        fbit = units[hour]+ " O'Clock"
    elif hour==10:
        fbit = "Ten O'Clock"
    else:
        fbit = teens[hour]+ " O'Clock"

print(fbit)
