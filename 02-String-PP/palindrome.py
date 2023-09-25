def check_palindrome(str):
    
    #remove spaces and convert to lowercase for case-senstive comprasion
    input_str = str.replace(" ","").lower()

    left = 0 
    right = len(input_str) - 1

    while left <= right:
        if input_str[left] != input_str[right]:
            return False
        left += 1
        right -= 1
    return True



str = input("Enter the string:  ")
if check_palindrome(str):
    print(f"{str} is a palidrome")
else:
    print(f"{str} is not palindrome")