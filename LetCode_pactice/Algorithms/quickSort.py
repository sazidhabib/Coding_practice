def quickSort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []
    
    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        
        else:
            items_lower.append(item)
    return quickSort(items_lower) + [pivot] + quickSort(items_greater)

number = [6,1,2,8,9,0,12,34,3,5,7]
print(quickSort(number))