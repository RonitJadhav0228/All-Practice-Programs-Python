def remove_duplicates(a):
    uniqure_char = []
    result =''
    for char in a:
        if char not in uniqure_char:
            uniqure_char.append(char)
            result = result + char
    return result

a = input("Enter the string:  ")
ans = remove_duplicates(a)
print(ans)