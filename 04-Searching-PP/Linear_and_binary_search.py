#python program to check element exist in the list 

#Linear search approach
def check_el(k,arr):
    for i in arr:
        if i == k:
            return True
        
    return False



arr = [1,14,23,33,13,12,19,20]
k = int(input("Enter the element :  "))

if check_el(k,arr):
    print(f"{k} exist in list")
else :
    print(f"{k} doesn't exist in list")



#binary search approach
def binary_search(k,arr):
    start = 0
    end = len(arr) - 1 

    while start <= end :
        mid = start + (end - start) // 2 
        if arr[mid] == k :
            return True
        elif arr[mid] < k:
            start = mid + 1 
        elif arr[mid] > k :
            end = mid - 1
    return False
    
#driver code
arr =[1,14,23,33,13,12,19,20]       
arr.sort()                                                
k = 19
if binary_search(k,arr):
    print(f"{k} exist in given list")
else:
    print(f"{k} doesn't exist in given list")
