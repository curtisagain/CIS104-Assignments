pennies = int(input('How many pennies do you have?'))
nickels = int(input('How many nickels do you have?'))
dimes = int(input('How many dimes do you have?'))
quarters = int(input('How many quarters do you have?'))
half_dollars = int(input('How many half dollars do you have?'))
dollars = int(input('How many one-dollar coins do you have?'))
#input results as int to avoid 3.0 pennies

change = float(pennies * 0.01) + float(nickels * 0.05) + float(dimes * 0.1) + float(quarters * 0.25) + float(half_dollars * 0.5) + (dollars)
change = str(round(change, 2))
# rounds to 2 decimal points. Solution from https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python

if pennies == 1: 
    print("You have 1 penny.")
else: 
    print("You have", int(pennies), "pennies.")
if nickels == 1: 
    print("You have 1 nickel.")
else: 
    print("You have", int(nickels), "nickels.")
if dimes == 1: 
    print("You have 1 dime.")
else: 
    print("You have", int(dimes), "dimes.")
if quarters == 1: 
    print("You have 1 quarter.")
else: 
    print("You have", int(quarters), "quarters.")
if half_dollars == 1: 
    print("You have 1 half dollar.")
else: 
    print("You have", int(half_dollars), "half dollars.")
if dollars == 1: 
    print("You have 1 dollar coin.")
else: 
    print("You have", int(dollars), "one-dollar coins.")
# all of the if/else is for grammar on output where the value is one.
print("The value of all of your coins is $" + str(change) + ".")
# printing as string fixes weird spacing issues.