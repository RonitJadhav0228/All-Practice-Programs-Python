
def is_vowel(str):
    char = str.lower()
    print(char)
    vowels = {'a','e','i','o','u'}
    if char in vowels:
        return print(f"{char} is vowel")
    else:
        return print(f"{char} is consonant")
    

#driver code
str = input("Enter the string:  ")
is_vowel(str)

# if len(str) == 1 and str.isalpha():
#     if is_vowel(str):
#         print(f"{str} is vowel")
#     else:
#         print(f"{str} is consonant")

