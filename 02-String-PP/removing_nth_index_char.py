def remove_ith_char(a,i,n):
    new_string = ''
    for j in range(n):
        if j == i  :
            str =  a.replace(a[i],'')
            new_string += str

    return new_string





a = input("Enter the string:  ")
i = int(input("Enter the ith element to remove from the list : "))
n = len(a)

result = remove_ith_char(a,i,n)
print(result)