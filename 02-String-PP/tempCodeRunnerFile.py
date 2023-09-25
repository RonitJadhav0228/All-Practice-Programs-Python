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