# using linear search to find index of peak element
def get_peak_element_linear(arr):
    n = len(arr)
    for i in range(n):
        if (i == n-1 or arr[i]>arr[i+1]) and (i == 0 or arr[i-1] < arr[i]):
            return i
    return -1

my_list = [1,3,20,4,1,0]
result1 = get_peak_element_linear(my_list)
if result1 != -1:
    print("Index of peak element is : ",result1)
else:
    print("No peak element found")

# using binary search to find index peak element
def get_peak_element_binary(arr):
    n = len(arr)
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low + (high-low)//2
        if ( mid == 0 or arr[mid-1]<arr[mid]) and ( mid == n-1 or arr[mid]>arr[mid+1]):
            return mid
        elif mid > 0 and arr[mid]> arr[mid-1]:
            low = mid + 1
        else:
            high = mid - 1
    return -1
result2 = get_peak_element_binary(my_list)
if result2 != -1:
    print("Index of peak element is : ",result2)
else:
    print("No peak element found")