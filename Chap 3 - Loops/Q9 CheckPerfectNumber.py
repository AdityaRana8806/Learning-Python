a = int(input("Enter a Number : "))
sum = 0
for i in range(1, a):
    if(a%i == 0):
        sum+=i
if(sum == a):
    print(f"{a} is a Perfect Number")
else:
    print(f"{a} is not a Perfect Number")