#This program will ask the user for three numbers then add them up and display them
sum = 0
#For item in range means how many times do they want it to happen
for item in range (0,3):
    #This is what tells the computer to ask for the numbers
    number= int( input ("Please enter number:"))
    #This adds up the three numbers
    sum = sum + number
    #This displays to the user what it equals
print("The answer is:",sum)

