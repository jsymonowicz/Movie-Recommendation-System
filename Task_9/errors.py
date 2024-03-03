# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")#SyntaxError: missing brackets in 'print()'
print("\n")#SyntaxError: missing brackets in 'print()', invalid tab

# Variables declaring the user's age, casting the str to an int, and printing the result#here I also deleted unnecessary tab for  clarity although it does not create an error
age_Str = "24 years old"#1) SyntaxError: invalid tab; 2) RuntimeError: '==' instead of '=', thus calling variable which was not declared
age = int(age_Str[0:2])#1) SyntaxError: invalid tab; 2) RuntimeError:"24 years old" cannot be int, thus I am taking only '24' out of "24 years old"
print("I'm " + str(age) + " years old.")#1) SyntaxError: invalid tab; 2) RuntimeError: 'age' is int and should be a string to be printed; 3) LogicalError: 'I'm24years old.' instead of 'I'm 24 years old.'

# Variables declaring additional years and printing the total years of age#here I also deleted unnecessary tab for clarity although it does not create an error
years_from_now = 3#SyntaxError: invalid tab; 2) RuntimeError: "3" is str and should be int
total_years = age + years_from_now#SyntaxError: invalid tab

print("The total age in "+ str(years_from_now)+" years from now: " + str(total_years))#1) SyntaxError: missing brackets in 'print()'; 2) LogicalError: "answer_years" should be total_years; 3) LogicalError: missing space after ':'; 4) RuntimeError: "answer_years" replaced by 'total_years' should be str(total_years) to be printed; 5) LogicalError: Message "The total number of years: " is unclear so I changed it

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 + 6#1) LogicalError: variables name is 'total_years' and not 'total'; 2) LogicalError: We print 'In 3 years and 6 months', so we must add another 6 months to total_months
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")#1) SyntaxError: missing brackets; 2) RuntimeError: total_months is not str so it cannot be printed

#HINT, 330 months is the correct answer