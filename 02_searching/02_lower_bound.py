# linear search for find lower bound
def linear_lower_bound(arr,x):
    for i in range(len(arr)):
        if arr[i]>= x:
            return i
    return i
my_list = [1,2,3,13,16,18,24,26,57,74]
result = linear_lower_bound(my_list,25)
print(result)

# binar search for finding lower bound
def binary_lower_bound(arr,x):
    low = 0
    high = len(arr)-1
    result = len(arr)-1
    while low <= high :
        mid = (low+high)//2
        if arr[mid] >= x:
            result = mid
            high = mid -1
        else:
            low = mid+1
    return mid
    
my_list = [1,2,2,4,4,4,4,7,9,11]
final_result = binary_lower_bound(my_list,3)
print(final_result)