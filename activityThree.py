'Purpose:Consider the string “Welcome to Python world”.Perform the following operations:
Count the number of alphabets in the given string.
To extract characters in the given, range from the given string.
Check if the string is alphanumeric or not.
Author: Humaira'


str="Welcome to Python world"
count=0
i=0
for j in str:
    if str[i].isalpha()==True:
        count=count+1
    i+=1
print(count)
print()
print(str[:8])
print()
str="Welcome to Python world"
if str.isalnum() is True:
    print("It is alphanumeric")
else:
    print("It is not alphanumeric")
