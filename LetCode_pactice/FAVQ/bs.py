def binarySeach(arr, target):
    left, right = 0, len(arr)-1

    
    while left <= right:
        mid = (left + right) //2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1




num = [10, 12, 15, 20, 23, 29, 36, 40, 52]
target = 40

print(binarySeach(num, target))