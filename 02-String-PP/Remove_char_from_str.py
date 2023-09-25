def remove_str(str,c):
    result = ""
    for char in str:
        if char != c :
            result = result + char
    return result

str = input("Enter the string :   ")
c = input("Enter the char you won't to remove  :  ")
result_string = remove_str(str,c)
print(result_string)