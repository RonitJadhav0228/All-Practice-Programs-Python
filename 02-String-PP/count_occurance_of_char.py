def count_occurance(str,c):
    count = 0 
    for char in range(len(str)) :
        if str[char] == c :
            count  = count + 1
    return count



str = input("Enter the string:   ")
c = input("Enter the char you won't to find the count of :  ")

result  = count_occurance(str,c)
print(result)

#check the both string are anagram or not - An anagram string can be define as a string that contains same characters but their order is different


def are_anagram(str1,str2):
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()

    if len(str1) != len(str2):
        return False
    
    char_count1 = {}
    char_count2 = {}
    

    for char in str1:
        if char in char_count1:
            char_count1[char] += 1 
        else:
            char_count1[char] = 1 
        
    for char in str2:
        if char in char_count2:
            char_count2[char] += 1 
        else:
            char_count2[char] = 1
        
    return char_count1 == char_count2



#driver code

str1 = input("Enter string1 : ")
str2 = input("Enter string2: ")
result = are_anagram(str1,str2)
if result:
    print(f"{str1} and {str2} are anagrams")
else:
    print(f"{str1} and {str2} are not anagrams")

