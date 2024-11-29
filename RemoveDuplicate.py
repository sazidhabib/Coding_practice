def remove_duplicates(nums):
    if not nums:
        return 0

    # Initialize a pointer for the unique elements
    k = 1

    for i in range(1, len(nums)):
        # If the current element is not equal to the last unique element
        if nums[i] != nums[k - 1]:
            nums[k] = nums[i]  # Place the unique element in the correct position
            k += 1

    return k

# Example usage
nums = [1, 1, 2,2,4,4,4,4,5,6,6,9]
k = remove_duplicates(nums)
print(k)          # Output: 2
print(nums[:k])   # Output: [1, 2]
