#Hugo North's Parking Meter Program

import time

print("Hello and Welcome to Sir Hugo North's Car Park")

time.sleep(1)

print("To park it is £5")

time.sleep(1)

print("Sorry today we only take 50p coins")

time.sleep(1)

print("To make the program work please type double the number of coins you would enter")

time.sleep(1)

print("Enter £5 IN 50p Coins")

time.sleep(1)

cash = 0

while cash < 5:
    time.sleep(1)
    coins = int(input("Please enter the money:"))
    cash = (cash + coins)
    print ("You have gave me {0} 50p coins".format(coins))
    money = cash / 2
    change = money - 5
    time.sleep(1)
    if change >= 0:
        print ("You entered {0} therefore your change is {1}".format(money,change))
        time.sleep(1)
        print ("Thank you very much for using Sir Hugo North's Car Park, I hope no one robbed your car. HAHAHA!")
    else:
        print ("You need to enter more money")
        #I am not sure how to loop the entering the money so this is all i have been able to do

        
        
    

    
