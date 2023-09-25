def len_str(a):
    counter = 0 
    for i in a:
         counter = counter + 1
    return counter

a = input("Enter the string: ")
print(len_str(a))