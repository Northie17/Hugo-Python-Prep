#This program will ask the user for three numbers then add them up and display them
import time
print ("Hello, This is my adding program by Hugo North.")
time.sleep(3)
print("I will ask you for three numbers, then add them up and tell you the answer")
sum = 0
#For item in range means how many times do they want it to happen
for item in range (0,3):
    #This is what tells the computer to ask for the numbers
    time.sleep(3)
    number= int( input ("Please enter the number:"))
    #This fills in the time
    print ("WORKING OUT YOUR NUMBER!")
    #This adds up the three numbers
    sum = sum + number
    #This displays to the user what it equals
time.sleep(3)
print("The answer of the three numbers is:",sum)
