#Hugo North's Parking Meter Program

import time

print("Hello and Welcome to Sir Hugo North's Car Park")

time.sleep(1)

print("To park it is £5")

time.sleep(1)

print("Enter £5 IN £1 Coins")

time.sleep(1)

cash = 0

while cash < 5:
    time.sleep(1)
    coins = int(input("Please enter the money:"))
    cash = (cash + coins)
    print ("You have gave me {0} pound coins".format(coins))
    money = cash
    change = money - 5
    time.sleep(1)

if change >= 0:
    print ("You entered {0} therefore your change is {1}".format(money,change))
    time.sleep(1)
    print ("Thank you very much for using Sir Hugo North's Car Park!")
    time.sleep(0.5)
    print ("Your change is dispensed below the screen area.")

else:
    coins = int(input("Please enter more money:"))
    cash = (cash + coins)
    print ("You have gave me {0} pound coins".format(coins))
    money = cash
    change = money - 5
    
    
