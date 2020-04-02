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

import numpy as np

# Convert txt to array
data = np.loadtxt("knapsack_big.txt").astype(int)
C = data[0, 0]
n = data[0, 1]
v = data[1:, 0]
s = data[1:, 1]
# Create dict and list to keep result
As = [[n, C]]
sol = As[0]
A = {(n, C): 0}

cnt = 0
while cnt < len(As):
    (n, c) = sol
    (n_idx, c_idx) = [n - 1, c], [n - 1, c-s[n - 1]]
    if n >= 1:
        if tuple(n_idx) not in A:
            As.append(n_idx)
            A[tuple(n_idx)] = 0
        if c >= s[n - 1]:
            if tuple(c_idx) not in A:
                As.append(c_idx)
                A[tuple(c_idx)] = 0
    sol = As[cnt]
    cnt += 1

for i in list(range(len(As) - 1, -1, -1)):
    (n, c) = As[i]
    if n == 0: continue

    if s[n - 1] > c:
        A[(n, c)] = A[(n - 1, c)]
    else:
        case_1 = A[(n - 1, c)]
        case_2 = A[(n - 1), c - s[n - 1]] + v[n - 1]
        A[(n, c)] = max(case_1, case_2)

answer_ex2 = A[(n, C)]



