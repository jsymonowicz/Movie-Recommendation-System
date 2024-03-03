#Ask user to enter his/her age:
age = int(input("Enter your age: "))

#Print message depending on entered age:
if age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")#assuming that here I should not add 'You're over the hill.' although 40 > 65
elif age >= 40:
    print("You're over the hill.")
elif age == 21:
    print("Congrats on your 21st!")
elif age < 13:
    print("You qualify for the kiddie discount.")
else:
    print("Age is just a number.")