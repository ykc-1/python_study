'''
输入某年某月某日，判断这一天是这一年的第几天？
'''
days=0
year=int(input("输入年\n"))
month=int(input("输入月\n"))
day=int(input("输入日\n"))
pin=[31,28,31,30,31,30,31,31,30,31,30,31]
run=[31,29,31,30,31,30,31,31,30,31,30,31]
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    for i in range(1,13):
        if month>i:
            days=days+run[i-1]
    days+=day
    print (days)
else:
    for i in range(1,13):
            if month>i:
                days=days+pin[i-1]
    days+=day
    print (days)