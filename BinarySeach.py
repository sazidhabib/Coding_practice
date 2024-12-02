def binary(array,target):
    left,right = 0, len(array)-1
    while left <= right:
        mid = (left + right)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid +1
        else:
            right = mid -1


array = [10,15, 20,25, 30, 40, 50]
target = 40
print(binary(array, target))

    