# 1. In this programming problem and the next you'll code up the knapsack 
# algorithm from lecture.

# Let's start with a warm-up. Download the text file below.

# knapsack1.txt
# This file describes a knapsack instance, and it has the following format:

# [knapsack_size][number_of_items]
# [value_1] [weight_1]
# [value_2] [weight_2]
# ...

# For example, the third line of the file is "50074 659", indicating that 
# the second item has value 50074 and size 659, respectively.
# You can assume that all numbers are positive. You should assume that 
# item weights and the knapsack capacity are integers.
# In the box below, type in the value of the optimal solution.
# ADVICE: If you're not getting the correct answer, try debugging your 
# algorithm using some small test cases. And then post them to 
# the discussion forum!

import numpy as np
# Convert txt to array
data = np.loadtxt("knapsack1.txt").astype(int)
C = data[0, 0]
n = data[0, 1]
v = data[1:, 0]
s = data[1:, 1]
A = np.zeros([n + 1, C + 1], int)

for i in range(1, n + 1):
    for c in range(0, C + 1):
        case_1 = A[i - 1, c]
        case_2 = A[i - 1, c - s[i - 1]] + v[i - 1]
        if s[i - 1] > c:
            A[i, c] = case_1
        else:
            A[i, c] = max(case_1, case_2)
            
answer_ex1 = A[n, C]

# 2.
# This problem also asks you to solve a knapsack instance, but a much bigger 
# one.

# Download the text file below.

# knapsack_big.txt
# This file describes a knapsack instance, and it has the following format:

# [knapsack_size][number_of_items]
# [value_1] [weight_1]
# [value_2] [weight_2]
# ...

# For example, the third line of the file is "50074 834558", indicating that 
# the second item has value 50074 and size 834558, respectively. As before, 
# you should assume that item weights and the knapsack capacity are integers.

# This instance is so big that the straightforward iterative implemetation 
# uses an infeasible amount of time and space. So you will have to be 
# creative to compute an optimal solution. One idea is to go back to a 
# recursive implementation, solving subproblems --- and, of course, caching 
#  results to avoid redundant work --- only on an "as needed" basis. 
# Also, be sure to think about appropriate data structures for storing and 
# looking up solutions to subproblems.

# In the box below, type in the value of the optimal solution.

# ADVICE: If you're not getting the correct answer, try debugging your 
# algorithm using some small test cases. And then post them to the 
# discussion forum!
