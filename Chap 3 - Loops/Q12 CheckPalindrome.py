a = input("Enter a Sentance : ")
b = ""
for i in range(len(a)-1, -1, -1 ):
    b+=a[i]

if(a == b):
    print("The Sentance is pallindrome")
else:
    print("Sentance is not a Pallindrome")
