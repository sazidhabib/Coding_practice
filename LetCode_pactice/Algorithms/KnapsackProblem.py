def knapsack(values, weights, capacity):
    n = len(values)

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]


    for i in range(1, n+1):
        for w in range(1, capacity + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w]= max(dp[i -1][w], dp[i-1][w-weights[i-1]] + values[i - 1])
    
    return dp[n][capacity]


values = [60,100,120]
weights = [10, 20, 30]
capacity = 50

print("Maximum value: ", knapsack(values,weights, capacity))



# def knapsack(values, weights, capacity):
#     n = len(values)  # Number of items
#     # Create a DP table with dimensions (n+1) x (capacity+1)
#     dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

#     # Build the table in bottom-up manner
#     for i in range(1, n + 1):  # Loop over items
#         for w in range(1, capacity + 1):  # Loop over weights
#             if weights[i - 1] > w:  # If item weight exceeds current capacity
#                 dp[i][w] = dp[i - 1][w]
#             else:  # Max of including or excluding the current item
#                 dp[i][w] = max(dp[i - 1][w],
#                                dp[i - 1][w - weights[i - 1]] + values[i - 1])

#     # The bottom-right cell contains the maximum value
#     return dp[n][capacity]


# # Example usage
# values = [60, 100, 120]  # Values of items
# weights = [10, 20, 30]   # Weights of items
# capacity = 50            # Maximum weight capacity of the knapsack

# print("Maximum value:", knapsack(values, weights, capacity))
