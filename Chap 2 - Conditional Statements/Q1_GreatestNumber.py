#Accept 2 numbers and print the greatest between them

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

if (num1 > num2):
    print(f"{num1} is the greater number")
elif(num2 > num1):
    print(f"{num2} is the greater number")
else:
    print("Both the numbers are equal")
    