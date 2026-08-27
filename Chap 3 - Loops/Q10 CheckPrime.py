a = int(input("Enter a Number : "))
c = 0
for i in range(1, a+1):
    if(a%i == 0):
        c+=1
if(c == 2):
    print(f"{a} is a Prime Number")
else:
    print(f"{a} is not a Prime Number")