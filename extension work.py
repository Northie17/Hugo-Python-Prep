number1 = float (input ("Please enter the number you would like to be squared:"))
answer1 = number1**2
print ("The square number of {0} is {1}".format(number1,answer1))              

number2 = float (input ("Please enter the number you would like to be cubed:"))
answer2 = number2**3
print ("The cubed number of {0} is {1}".format(number2,answer2))


number3 = float (input ("Please enter the length of one side of the square:"))
answer3 = number3*4
print ("The perimeter of a square with a side {0} is {1}".format(number3,answer3))

number4 = float (input ("Please enter the length of the two longest sides of the rectangle:"))
number5 = float (input ("Please enter the length of the two shortest sides of the rectangle:"))
answer4 = number4*number5
print ("The perimeter of a rectangle with two sides of {0} and two sides of {1} is {2}".format(number4,number5,answer4))

number6 = float (input ("Please enter the length of one side of the square:"))
answer5 = number6**2
print ("The area of a square with a side {0} is {1}".format(number6,answer5))

number7 = float (input ("Please enter the length of one side of the cube:"))
answer6 = 6*number7**2
print ("The area of a cube with one side {0} is {1}".format(number7,answer6))
1.11
number8 = float (input ("Please enter the number of pounds you would like to be converted:"))
answer7 = number8*1.11

print (" £{0:.2f} exchanges to €{1:.2f}".format(number8,answer7))
