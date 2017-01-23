import time
print("This program changes binary to denary")
BinaryNumber = (input("Please enter your 8 digit binary number"))
print("Processing")
time.sleep(1)
# Algorithm of Two's Complement program:
# First number * -128 then normal binary to denary program
DenaryNumber = ((int(BinaryNumber[0]) *-128) + (int(BinaryNumber[1]) *64) + (int(BinaryNumber[2]) *32) + (int(BinaryNumber[3]) *16)) + (int(BinaryNumber[4]) *8) + (int(BinaryNumber[5]) *4) + (int(BinaryNumber[6]) *2) + (int(BinaryNumber[7]) *1)
print("The two's complement of your number is: ",DenaryNumber)
