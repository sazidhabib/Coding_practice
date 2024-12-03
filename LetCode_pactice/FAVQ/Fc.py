def FrequencyCount(arr):
    count ={}

    for num in arr:
        if num in count:
            count[num] +=1
        else:
            count[num] = 1
    return count


number = [1,1,1,1,3,3,3,3,5,5,5,4,7,7,7,]
print(FrequencyCount(number))