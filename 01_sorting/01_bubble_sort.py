def bubblesort(arr):
    n = len(arr)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
list = [12,3,25,9,4,1]
print(bubblesort(list))



# Given an array of integers, sort the array in ascending order using Bubble Sort.
# Input: [5, 2, 9, 1, 5, 6]
# Expected Output: [1, 2, 5, 5, 6, 9]
def bubblesort(arr):
    n= len(arr)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
list = [5, 2, 9, 1, 5, 6]
print(bubblesort(list))


# Given an array of integers, sort it in descending order using Bubble Sort.
# Input: [3, 1, 4, 2, 8]
# Expected Output: [8, 4, 3, 2, 1]
def bubblesort(arr):
    n= len(arr)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
list = [3, 1, 4, 2, 8]
print(bubblesort(list))



# Sort the array using Bubble Sort and also return the total number of swaps made.
# Input: [4, 3, 1, 2]
# Expected Output: Sorted array: [1, 2, 3, 4], Swaps: 5
def bubblesort(arr):
    n= len(arr)
    count = 0
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                count += 1
    print(arr)
    print(count)
list = [4, 3, 1, 2]
bubblesort(list)



# Modify Bubble Sort to stop early if the array is already sorted before all passes.
# Input: [1, 2, 3, 4, 5]
# Expected Output: Only 1 pass, array remains same
def bubblesort(arr):
    n= len(arr)
    for i in range(0,n-1):
        count = 0
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                count += 1
        if count == 0:
            break
    return arr
list = [1, 2, 3, 4, 5]
print(bubblesort(list))



# Given a list of strings, sort them by their length using Bubble Sort.
# Input: ["apple", "hi", "banana", "a"]
# Expected Output: ["a", "hi", "apple", "banana"]
def bubblesort(arr):
    n= len(arr)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if len(arr[j])>len(arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
list = ["apple", "hi", "banana", "a"]
print(bubblesort(list))


# Sort and Find K-th Largest Element (using Bubble Sort)
# Input: [7, 4, 6, 3, 9, 1], k = 3
# Output: 6
def bubblesort(arr,x):
    n= len(arr)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr[x-1]
list = [7, 4, 6, 3, 9, 1]
print(bubblesort(list,3))




# sort a string in decreasing order of value associated after removal of value smaller than x

def sortString(str,x):
    my_list = str.split()
    n = len(my_list)
    empty_list = []
    for i in range(1,n+1,2):
        value = int(my_list[i])
        name = my_list[i-1]
        if value >= x:
            empty_list.append(name)
            empty_list.append(value)
    n = len(empty_list)
    print(empty_list)
    print(n)
    for i in range(1,n-1,2):
        for j in range(1,n-i-1,2):
            if  (empty_list[j] < empty_list[j+2]) or (empty_list[j-1] > empty_list[j+1] and empty_list[j] == empty_list[j+2]):
                 empty_list[j],empty_list[j+2]=empty_list[j+2],empty_list[j]
                 empty_list[j-1],empty_list[j+1]=empty_list[j+1],empty_list[j-1]
    print(empty_list)
sortString("Anjani 73 ravi 97 prince 99 dinesh 90 deepu 93 pankaj 97 unknown 13",90)





# Sort Student Records (Name + Marks) Using Bubble Sort
# Input: [["Raj", 88], ["Anu", 92], ["Pooja", 75], ["Vikram", 88]]

# Output (descending by marks, name ascending if same):
# [['Anu', 92], ['Raj', 88], ['Vikram', 88], ['Pooja', 75]]
def student_record(arr):
    new_list =[]
    for el in arr:
        for j in el:
            new_list.append(j)
    n = len(new_list)
    for i in range(1,n-1,2):
        for j in range(1,n-1-i,2):
             if (new_list[j] < new_list[j+2]) or (new_list[j-1] > new_list[j+1] and new_list[j] == new_list[j+2]):
                 new_list[j],new_list[j+2]=new_list[j+2],new_list[j]
                 new_list[j-1],new_list[j+1]=new_list[j+1],new_list[j-1]
    final_list = []
    for i in range(0,n,2):
        created_list = []
        created_list.append(new_list[i])
        created_list.append(new_list[i+1])
        final_list.append(created_list)
    print(final_list)

student_list = [["Raj", 88], ["Anu", 92], ["Pooja", 75], ["vikram", 88]]
student_record(student_list)