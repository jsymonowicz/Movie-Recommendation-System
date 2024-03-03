'''
This code executes two programs which read in a string and:
Program 1: converts alternate LETTERS to upper and lower case.
Program 2: converts alternate WORDS to upper and lower case.
'''

#Read in a string
sentence = input("Enter a string: ")

##### Program 1 #####

#Create a list to convert letters into upper and lower case
program_1 = []

for i in range(len(sentence)):
#Even letters are converted upper case
    if i % 2 == 0:
        program_1.append(sentence[i].upper())
#Odd letters are converted lower case
    else:
        program_1.append(sentence[i].lower())
        
#Join letters and print them out:
print("".join(program_1))

##### Program 2 #####

#Split sentence into a list with separate words:
program_2 = sentence.split(' ')

for i in range(len(program_2)):
#Even words are converted lower case
    if i % 2 == 0:
        program_2[i] = program_2[i].lower()
#Odd words are converted upper case
    else:
        program_2[i] = program_2[i].upper()
        
#Join words and print out a sentence:
print(" ".join(program_2))

'''
Test sentences:
Hello World
I am learning to code
'''