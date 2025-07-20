# Selection sort
list = [64,25,172,22,101]
n = len(list)
for i in range(n-1):
    min_index = i
    for j in range(i+1,n):
        if list[min_index] > list[j]:
            min_index= j
    list[min_index],list[i]=list[i],list[min_index]
print(list)

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[min_index]>arr[j]:
                min_index=j
        arr[min_index],arr[i]=arr[i],arr[min_index]
    return arr
print(selection_sort(list))

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[min_index]>arr[j]:
                min_index = j
        arr[min_index],arr[i]=arr[i],arr[min_index]
    return arr