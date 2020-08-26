#Lab 2 from week 3 of the Basics of Computing and Programming from NYUx
#Author: relentlesss

print('Please enter the amount of money to convert: ')

dollars = int(input('# of dollars: '))
cents = int(input('# of cents: '))

quarters = 0
quarter = 0
dimes = 0
nickels = 0
pennies = 0

quarters += int(dollars/0.25)

if cents / 25 >= 1:
    quarter += int(cents / 25)
    cents -= 25 * quarter
if cents / 10 >= 1:
    dimes += int(cents / 10)
    cents -= 10 * dimes
if cents / 5 >= 1:
    nickels += int(cents / 5)
    cents -= 5 * nickels
if cents / 1 >= 1:
    pennies += int(cents / 1)
    cents -= 1 * pennies

fullquart = quarters + quarter

print('The coins are', fullquart, 'quarters,', dimes, 'dimes,', nickels, 'nickels and', pennies, 'pennies'  )
