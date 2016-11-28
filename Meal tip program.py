Name = input ("Please enter your name:")
Meal = float (input ("Please enter cost of meal:" ))
PercentTip = float (input ("Please enter percentage of tip :" ))

Tip = Meal/PercentTip
TotalCost = Meal + Tip

print ("The total cost for your meal is £{0:.2f} as the tip is £{1:.2f}".format(TotalCost,Tip))
print ("Thank you {0} for using this Meal Tip Calculator".format(Name))

