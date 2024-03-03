#Ask user to enter name of his/her favourite restaurant
string_fav = input("Enter the name of your favourite restaurant: ")

#Ask user to enter his/her favourite number
int_fav = int(input("Enter your favourite number: "))

#Print out two above statements:
print(f"Your favourite restaurant is {string_fav}")
print(f"Your favourite number is {int_fav}")

#Casting string_fav to an integer:
string_fav = int(string_fav)
'''
Casting of a string name of a resturant to an integer causes error: 'ValueError: invalid literal for int() with base 10' because int data type requires numbers and not letters!
'''