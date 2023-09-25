def delete_vowels(string):
    result =''
    vowels = 'aeiou'
    for char in string:
        if char in vowels:
            char = ''

        result += char
    print("String after removing vowels : ",result)


string = input('Enter the string: ')
delete_vowels(string)