#WAP to check if the input year is a leap year or not

y = int(input("Enter year : "))

if (y%4 == 0) and (y%100 != 0):
    print(f"{y} is a Leap Year")
elif (y%4 == 0) and (y%100 == 0) and (y%400 == 0):
    print(f"{y} is a Leap Year")
else :
    print(f"{y} is Not a Leap Year")
