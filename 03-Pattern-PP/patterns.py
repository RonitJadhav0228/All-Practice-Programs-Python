#Simple Number Triangle pattern
def pattern01(n):
    for row in range(n):
        for i in range(row):
            print("*",end = " ")
        print(" ")




def pattern2(n):
    for row in range(n):
        for i in range(n+1):
            print("*",end = " ")
        print(" ")

def pattern03(n):
    r = 0 
    for i in range(n-r):
        
        for j in range(n-i):
            print("* ",end=" ")
        print(" ")
        
def pattern04(n):
    for i in range(1,n+1):
        for j in range(i):
            print(j,end=" ")
        print(" ")

def pattern05(n):
    for i in range(1,n+1):
        print("*" * i)

    for i in range(n-1,0,-1):
        print('*'*i)
   
def pattern06(n):
    for i in range(1,n+1):
        print(" "*(n-i), end=" " )

        print("*"*i)

def pattern07(n):
    for i in range(n,0,-1):
        print(" " * (n-i),end=" ")

        print("*" * i)


        
  
n = int(input("Enter the n: "))
pattern01(n)

print("New pattern\n")
pattern2(n)

print("\n New pattern")
pattern03(n)

print("\n New pattern")
pattern04(n)

print("\n New pattern")
pattern05(n)

print("\n New pattern")
pattern06(n)

print("\n New pattern")
pattern07(n)


print("\n New pattern")
pattern08(0,n)







