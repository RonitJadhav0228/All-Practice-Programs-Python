def reverse(a):
    reverse_str = '' # initalizing emty string
    for char in a :
        reverse_str = char + reverse_str
    return reverse_str




a = input("Enter the string:  ")
print(reverse(a))


