# binary search
myList = [1,2,3,4,5,6]
start = 0
end = len(myList)-1
x = 6

while start <= end:

        mid = start + (end - start)//2

        if myList[mid] == x:
            print(mid)
            break

        elif myList[mid] < x:
            start = mid + 1

        else:
            end = mid - 1

if myList[mid] != x:
    print("Not found in the list")
