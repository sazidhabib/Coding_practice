def top_k_frequent(nums, k):

    frequency_map = {}
    for num in nums:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1


    sorted_items = sorted(frequency_map.items(), key=lambda x: x[1], reverse=True)

    result = []
    for i in range(k):
        result.append(sorted_items[i][0])

    return result

nums = [3, 3, 3, 5, 5, 4]
k = 2
result = top_k_frequent(nums, k)
print("The top K frequent elements are:", result)


# def top_k_frequent(nums, k):
#     """
#     Finds the top K frequent elements in a list.

#     Parameters:
#         nums (list): List of integers.
#         k (int): Number of top frequent elements to return.

#     Returns:
#         list: List of the top K frequent elements.
#     """
#     # Step 1: Count the frequency of each number
#     frequency_map = {}
#     for num in nums:
#         if num in frequency_map:
#             frequency_map[num] += 1
#         else:
#             frequency_map[num] = 1

#     # Step 2: Sort elements by frequency in descending order
#     sorted_items = sorted(frequency_map.items(), key=lambda x: x[1], reverse=True)

#     # Step 3: Extract the top K elements
#     result = []
#     for i in range(k):
#         result.append(sorted_items[i][0])

#     return result

# # Example usage
# nums = [1, 1, 1, 2, 2, 3]
# k = 2
# result = top_k_frequent(nums, k)
# print("The top K frequent elements are:", result)
