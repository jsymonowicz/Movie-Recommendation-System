#Ask user to enter 3 different integers
num_1 = int(input("Please, enter an integer: "))
num_2 = int(input("Please, enter a different integer: "))
num_3 = int(input("Please, enter yet another integer: "))

#sum of numbers:
num_sum = num_1 + num_2 + num_3
print(f"Sum of your numbers is {num_sum}")

#num_1 - num_2
num_diff = num_1 - num_2
print(f"The 1st number minus the 2nd number is: {num_diff}")

#num_3 * num_1
num_multiply= num_3 * num_1
print(f"The 3rd number multiplied the 1st number is: {num_multiply}")

#sum of numbers / num_3
num_sum_div= num_sum / num_3
print(f"The sum of numbers divided by the 3rd number is: {num_sum_div}")