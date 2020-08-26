#Lab 1 from week 3 of the Basics of Computing and Programming from NYUx
#Author: relentlesss

print("Please enter the number of coins:")

quarters = int(input("# of quarters: "))
dimes = int(input("# of dimes: "))
nickels = int(input("# of nickels: "))
pennies = int(input("# of pennies: "))

total = round((quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01), 2)

whole = int(total)

dec = round(total - whole, 2)*100
dec_up = int(dec)

print("The total is", str(whole), "dollars and", str(dec_up), "cents")
