def count_vowels_consontant(string):
    count_vowels = 0
    count_consontant = 0
    vowels = 'aeiou'
    for char in string:
        if char in vowels:
            count_vowels += 1
        else:
            count_consontant += 1
        
    print(f"{count_vowels} is the count of vowels in the given string")
    print(f"{count_consontant} is the count of consontant in the given string")
        

string = input("Enter the string :  ")
count_vowels_consontant(string)


