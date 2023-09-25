#Program to print even len words in the string
# Input string
input_string = input("Enter a string: ")

# Split the input string into words
words = input_string.split()

# Iterate through the words and print even-length words
print("Even-length words in the string:")
for word in words:
    if len(word) % 2 == 0:
        print(word)


#program that accepts all the vowels
def all_vowels(str):
    str = str.replace(" ","")
    str = str.lower()
    vowels = [str.count('a'),str.count('e'),str.count('i'),str.count('o'),str.count('u')]
    if vowels.count(0) > 0:
        print("not accepted")
    else:
        print('Accepted')
        
str = input("Enter the string:   ")
all_vowels(str)

