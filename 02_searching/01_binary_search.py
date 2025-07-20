def searching(arr,x):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            high = mid-1
        else:
            low = mid+1
    return

my_list = [1,2,3,13,16,18,24,26,57,74]
result  = searching(my_list,57)
if result == -1:
    print("No record found")
else:
    print("target found at index :",result)

# using recursion
def recursion_searching(arr,low,high,x):
    mid = (low+high)//2
    if low > high:
        return -1
    else:
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return recursion_searching(arr,low,mid-1,x)
        else:
            return recursion_searching(arr,mid+1,high,x)
my_list = [1,2,3,13,16,18,24,26,57,74]
result  = recursion_searching(my_list,0,len(my_list)-1,57)
if result == -1:
    print("No record found")
else:
    print("target found at index :",result)