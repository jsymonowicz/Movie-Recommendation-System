# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"#Runtime Error: Lion should be a string
animal_type = "cub"
number_of_teeth = 16

#Logical Error: if word starts with a, e, i, o, then it is preceded by 'an', so I am adding a functionality taking this into account
#new funtionality starts here
vowels = ["a", "e", "i", "o"]

if animal[0].lower() in vowels:
    article_1 = 'an'
else:
    article_1 = 'a'    
    
if animal_type[0].lower() in vowels:
    article_2 = 'an'
else:
    article_2 = 'a' 
#new funtionality ends here

print(f"This is {article_1} {animal}. It is {article_2} {animal_type} and it has {number_of_teeth} teeth.")#1) Syntax Error: missing () in print(); 2) #Runtime Error: full_spec was moved to print() so that we can display values in {}; 3) Logical Error: 'number_of_teeth' exchanged with 'animal_type'