#Check if two arrays are equal

def array_equal(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

arr1 = [1,2,3]
arr2 = [1,2,3]
print(array_equal(arr1, arr2))
