#Ask user for the sentence
str_manip = input("Please, enter a sentence: ")

#print length of the sentence
str_manip_length = len(str_manip)
print(f"The length of your sentence is {str_manip_length} characters.")

#find the last letter of the sentence
last_char = str_manip[-1]
#replace every occurence of last_char with "@"
str_manip_with_at = str_manip.replace(last_char, "@")
print(str_manip_with_at)

#print last 3 characters in str_manip backwards
last_3_chars_backwards = str_manip[-1:-4:-1]
print(last_3_chars_backwards)

#Combine first 3 and last 2 characters of str_manip into a word
new_word = str_manip[0:3] + str_manip[-2::]
print(new_word)