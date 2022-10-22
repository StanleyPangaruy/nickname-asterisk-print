
# Assignment 1:
# Create a program that will print your nickname using only asterisk character (*)

#This is a 2-dimensional array containing the letter pattern of the nickname.
arrStan = [[0,1,1,1,0,0,1,1,1,1,1,0,0,1,1,1,0,0,1,0,0,0,1],
           [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,1,0,0,1],
           [1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,1,0,0,1],
           [0,1,1,1,0,0,0,0,1,0,0,0,1,1,1,1,1,0,1,0,1,0,1],
           [0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,1,1], 
           [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,1,1],
           [0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1]]

#Iterates each elements in the array
for i in arrStan:
    for j in i:
        #Changes the elements to an intended string. 
        if j == 1:
            print("*", end=" ")
        else: 
            print(" ", end=" ")
    print()