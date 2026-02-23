year=int(input("enter year:"))
if (year%4==0) and (year %100!=0 or year%400==0):
    print(year,"is leap")
else:
    print("not a leap year")