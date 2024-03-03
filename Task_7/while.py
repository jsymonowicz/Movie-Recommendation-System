'''
This program asks a user to enter a number until '-1' is entered.
The program then calculates the average of entered numbers excluding -1.
'''

#declaring variables needed to calculate numbers average
number_sum = 0
count = 0

#asking to enter a number until -1 is entered and adding this number to number_sum:
while True:
    number = float(input("Enter a number: "))
    if number == -1:
        break
    number_sum += number
    count += 1
    
#calculating the average of the numbers entered:
number_average = number_sum / count
print(number_average)