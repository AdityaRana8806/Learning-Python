#WAP to take input of gender of user and print a greeting message

G = input("Enter your Gender : ")

if (G == 'Male') or (G == 'male') or (G == 'M') or (G == 'm'):
    print("Good Afternoon Sir")
elif (G == 'Female') or (G == 'female') or (G == 'F') or (G == 'f'):
    print("Good Afternoon Madam")
else : 
    print("Gender not specified")