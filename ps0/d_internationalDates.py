"""
Right - quite an interesting practical problem. 

Higher level logic: 
1. If the first part of date is > 12, and 2nd part is <= 12, then EU. 
2. If 1st part <=12 and 2nd part > 12, then US
3. Else: either 
"""
dateString = input()
date = dateString.split('/')
dateInt = [int(i) for i in date]

if dateInt[0] > 12 and dateInt[1] <=12:
    print('EU')
elif dateInt[0] <= 12 and dateInt[1] > 12:
    print('US')
else:
    print('either')

