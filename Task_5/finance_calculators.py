'''
This program includes two different financial calculators:
    1. investment
    2. home loan repayment (bond)
The user chooses which calculator to use.
The 'investment' calculator outputs the total amount with applied interest.
The 'bond' calculator outputs amount to be repaid on a home loan each month.
'''

#Importing necessary libraries
import math

#Choosing which calculator to use
print("investment\t - to calculate the amount of interest you'll earn on your investment\nbond\t\t - to calculate the amount you'll have to pay on a home loan")
option = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
option = option.lower()#Removing capitalisation

#Assuring that the chosen option is valid:
while (option != "investment") and (option != "bond"):
    option = input("Error: invalid option. Enter either 'investment' or 'bond' to proceed: ")
    option = option.lower()#Removing capitalisation

##########Investment calculator##########
if option == 'investment':
#Ask for the amount of deposited money
    deposit = float(input("Enter the amount of money you want to deposit [£]: "))
#Ask for the interest rate
    rate = float(input("Enter the interest rate [%]: "))
    rate = rate / 100#Recalculate from %
#Ask for the number of years of investment
    years = int(input("Enter number of years of investment: "))
#Select 'simple' or compound interest
    interest = input("Select simple or compound interest: ")
    interest = interest.lower()#Removing capitalisation
#Assuring that the chosen interest option is either 'simple' or 'compound'
    while (interest != "simple") and (interest != "compound"):
        interest = input("You selected wrong interest type. Please, select 'simple' or 'compound': ")
        interest = interest.lower()#Removing capitalisation
#Calculate amount with applied interest for 'simple' interest
    if interest == "simple":
        amount = deposit * (1 + (rate * years))
        amount = round(amount, 2)#Rounding to 2 digits after ','
        print(f"Total amount with applied interest: £{amount}")
#Calculate amount with applied interest for 'compound' interest
    else:
        amount = deposit * math.pow((1 + rate), years)
        amount = round(amount, 2)#Rounding to 2 digits after ','
        print(f"Total amount with applied interest: £{amount}")
             
##########Bond calculator##########
else:
#Ask for the value of the house
    house_value = float(input("Enter value of the house [£]: "))
#Ask for the interest rate
    rate = float(input("Enter the interest rate [%]: "))
    rate = rate / 100#Recalculate from %
#Ask for the number of months over which the bond will be paid
    months = int(input("Enter number of months over which the bond will be paid: "))
#Calculate amount to be repaid on a home loan each month
    i = rate / 12#Monthly interest rate
    repayment = (i * house_value) / (1 - (1 + i)**(-months))
    repayment = round(repayment, 2)#Rounding to 2 digits after ','
    print(f"Amount to be repaid on a home loan each month: £{repayment}")