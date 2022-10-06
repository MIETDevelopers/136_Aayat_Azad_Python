# Linear Search
myList = [6,7,8,9,10,11,12]
value = input("Enter the value:")
value = int(value)
for i in range(0, len(myList)):
    if myList[i] == value:
        print("Item found at : ",i )
        break
if myList[i] != value:
    print("Element not present in the list")
