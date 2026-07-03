#String Indexing starts with 0 from left and -1 from Left

a = "I am going to start my College"
print (a[0]) #This Prints the character on zeroth index

#String Slicing = to take out a specific portion from a string
# print (Start point : Stop Point : )
print (a[0:19:2]) #this prints all the letters from 0th index till (19-1)th index with a jump of 2
print (a[26 : 29 : 1]) #this prints all the letters from 26th index till (29-1)th index with a jump of 1

#To Just prin "Clee" we can write the following code
print (a[23 : 30 : 2]) 