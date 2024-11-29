def remove_element(nums, val):
    # Pointer to track the position for non-val elements
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k

# Example usage
nums = [3, 2, 2, 3]
val = 3
k = remove_element(nums, val)
print(k)         # Output: 2
print(nums[:k])  # Output: [2, 2]
