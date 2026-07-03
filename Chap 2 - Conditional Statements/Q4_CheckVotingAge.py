#Question 1 : WAP to take input of age and check if the person can vote or not

age = int(input("What is your Age : "))
if (age >= 18) :
    print(f"Since your age is {age} YOU ARE ELIGIBLE to vote")
else :
    print(f"Since your age is {age} you are NOT eligible to vote")
