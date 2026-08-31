a = input("Enter any Random Sentence : ")

char = 0
spchar = 0
digit = 0

for i in range (a):
    if i.isdigit():
        digit+=1
    elif i.isalpha():
        