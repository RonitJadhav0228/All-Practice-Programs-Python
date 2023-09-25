n = int(input("Enter the number: "))
sum = 0 
temp = n 

#Count of the number of digit in input

count = len(str(n))
while temp > 0 :
    digit = temp % 10 
    sum += digit ** count
    temp //= 10 

if n == sum :
    print("Given ",n,"is an Armstrong number")
else:
    print("Given",n,"is not an Armstrong Number")