def deleteElement(arr, i):
    arr2 = []
    if i < 0 or i >= len(arr):
        print("Invalid index.")
        return arr
    
    for j in range(len(arr)):
        if j != i:
            arr2.append(arr[j])
    
    return arr2

arr = [3, 7, 1, 9, 4]
delete_index = 2
new_array = deleteElement(arr, delete_index)
print("new array =", new_array)