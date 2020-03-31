# 1.Question 1
# In this assignment you will implement one or more algorithms for 
# the all-pairs shortest-path problem. Here are data files describing 
# three graphs:

# g1.txt
# g2.txt
# g3.txt
# The first line indicates the number of vertices and edges, respectively. 
# Each subsequent line describes an edge (the first two numbers are its tail 
# and head, respectively) and its length (the third number). NOTE: some of 
#  edge lengths are negative. NOTE: These graphs may or may not have 
# negative-cost cycles.

# Your task is to compute the "shortest shortest path". Precisely, you must 
# first identify which, if any, of the three graphs have no negative cycles. 
# For each such graph, you should compute all-pairs shortest paths and 
# remember the smallest one (i.e., compute minu,v∈Vd(u,v), where d(u,v)d(u,v) 
# denotes the shortest-path distance from uu to vv).

# If each of the three graphs has a negative-cost cycle, then enter "NULL" 
# in the box below. If exactly one graph has no negative-cost cycles, then 
# enter the length of its shortest shortest path in the box below. If two or 
# of the graphs have no negative-cost cycles, then enter the smallest of the 
# lengths of their shortest shortest paths in the box below.

# OPTIONAL: You can use whatever algorithm you like to solve this question. 
# If you have extra time, try comparing the performance of different 
# all-pairs shortest-path algorithms!

# OPTIONAL: Here is a bigger data set to play with.

# large.txt
# For fun, try computing the shortest shortest path of the graph in the 
# file above.

import numpy as np

# Create a list of integers from txt-file
fh = open("g3.txt", "r") #change name of file here
list_str = fh.readlines()
fh.close()
#Create a dict of dicts for adjacency list representetoin
G = {node: {} for node in range(1, 1001)}
for line in list_str[1:]:
    node_1 = int(line.split()[0])
    node_2 = int(line.split()[1])
    weight = int(line.split()[2])
    G[node_1][node_2] = weight

n = 1000
# Create 3D-array
A = np.zeros([n, n, n])
# Base cases
for i in range(n):
    for v in range(n):
        if i == v:
            A[i, v, 0] = 0
        elif v + 1 in G[i + 1]:
            A[i, v, 0] = G[i + 1][v + 1]
        else:
            A[i, v, 0] = np.inf
# Fot others verts
for k in range(1, n):
    if k % 100 == 0:
        print('num of iteration:', k)
    for i in range(n):
        for v in range(n):
            case_1 = A[i, v, k - 1]
            case_2 = A[i, k, k - 1] + A[k, v, k - 1]
            A[i, v, k] = min(case_1, case_2)
# Find negative cycles and mins
neg_list = []
for i in range(n):
    if A[i, i, n - 1] < 0:
        neg_list.append(i + 1)
        print('negative cycle in node:', i+1)
#ssp - shortest shortest path
min_G = A[:, :, n - 1].min()
print('min of A:', min_G)

# Algo is slow for big arrays, thefore kept result
# g1.txt
# min of A: -2.0713167043626029e+189

# g2.txt
# min of A: -3.8997021614875794e+168

# g3.txt
# min of A: -19.0 - no negative cycles

        

            
            
            
            