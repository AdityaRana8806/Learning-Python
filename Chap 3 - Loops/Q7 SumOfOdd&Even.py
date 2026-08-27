a = int(input("Enter Starting Limit: "))
b = int(input("Enter Ending Limit : "))
so = 0; se = 0
for i in range(a, b+1):
    if(i%2==0):
        se+=i
    else:
        so+=i
print(f"Sum of all Even Numbers = {se} and Sum of all Odd Numbers = {so}")