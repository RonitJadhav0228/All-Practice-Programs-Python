def lower_vowels_to_uppercase(string):
    # vowels = {'a','e','i','o','u'}
    vowels ='aeiou' #vowels
    for char in string:
        if char in vowels:
            upper_char = char.upper() #converting lower case to upper case

            string = string.replace(char,upper_char) #Replacing lower case vowels to upper case
    print(f"Updated string {string}")


string = input('Enter the string: ')
lower_vowels_to_uppercase(string)