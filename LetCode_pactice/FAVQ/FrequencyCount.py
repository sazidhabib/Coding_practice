def frequencyCount(arr):
    frequency = {}

    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency

arr = [1,2,2,3,4,4,4,5,5,5,5,1,1,1,]
result = frequencyCount(arr)
print(result)