def special_char(a):
    a.split()
    c = 0 
    s = '[@_!#$%^&*()<>?/\|}{~:]'
    for i in range(len(a)):
        if a[i] in s:
            c += 1 #if specil char found then add one
    
    if c:
        print('String accepeted')
    else:
        print("String won't be accepted")

        
a = input("Enter the string: ")
special_char(a)