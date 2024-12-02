def findMissingNumber(arr):
    n = len(arr) + 1 
    full_xor = 0
    arr_xor = 0

    for i in range(1, n+1):
        full_xor ^= i
    
    for num in arr:
        arr_xor ^=num
    
    return full_xor ^ arr_xor

arr =[1,2,3,5]
print(findMissingNumber(arr))
