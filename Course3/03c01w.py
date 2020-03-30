# 1. In this programming problem and the next you'll code up the greedy 
# Download the text file below.
# algorithms from lecture for minimizing the weighted sum of completion 
# times..


# jobs.txt
# This file describes a set of jobs with positive and integral weights 
# and lengths. It has the format
# [number_of_jobs]
# [job_1_weight] [job_1_length]
# [job_2_weight] [job_2_length]
# ...

# For example, the third line of the file is "74 59", indicating that
# the second job has weight 74 and length 59.

# You should NOT assume that edge weights or lengths are distinct.

# 1. Your task in this problem is to run the greedy algorithm that schedules 
# jobs in decreasing order of the difference (weight - length). 
# Recall from lecture that this algorithm is not always optimal. 

# IMPORTANT: if two jobs have equal difference (weight - length), 
# you should schedule the job with higher weight first. 

# Beware: if you break ties in a different way, you are likely to get 
# the wrong answer. 

# You should report the sum of weighted completion times 
# of the resulting schedule --- a positive integer --- in the box below.

# ADVICE: If you get the wrong answer, try out some small test cases to 
# debug your algorithm (and post your test cases to the discussion forum).

import copy

# Create a list of integers from txt-file
fh = open("jobs.txt", "r") 
list_str = fh.readlines()
fh.close()
wei_len = []
for line in list_str[1:]:
    lst_int = [int(el) for el in line.strip().split()]
    wei_len.append(lst_int)
    
wei_len_1 = copy.deepcopy(wei_len)
# Sort for easy work with condition 'you should schedule the job with 
# higher weight first.'
wei_len_1.sort(key=lambda x: x[0], reverse=True)
# decreasing order of the difference (weight - length)
wei_len_1.sort(key=lambda x: x[0]-x[1], reverse=True)
# Count the sum of weighted completion times
len_sum_1 = 0
w_comp_t_1 = 0
for line in wei_len_1:
    len_sum_1 += line[1]
    w_comp_t_1 += len_sum_1*line[0]

answer_ex1 = w_comp_t_1
# 2. For this problem, use the same data set as in the previous problem.

# Your task now is to run the greedy algorithm that schedules jobs 
# (optimally) in decreasing order of the ratio (weight/length). 
# In this algorithm, it does not matter how you break ties. You should 
# report the sum of weighted completion times of the resulting schedule --- 
# a positive integer --- in the box below.
wei_len_2 = copy.deepcopy(wei_len)
# decreasing order of the ratio (weight/length)
wei_len_2.sort(key=lambda x: x[0] / x[1], reverse=True)
# Count the sum of weighted completion times
len_sum_2 = 0
w_comp_t_2 = 0
for line in wei_len_2:
    len_sum_2 += line[1]
    w_comp_t_2 += len_sum_2*line[0]

answer_ex2 = w_comp_t_2

# 3. In this programming problem you'll code up Prim's minimum spanning 
# tree algorithm.

# Download the text file below.

# edges.txt
# This file describes an undirected graph with integer edge costs. It has 
# the format

# [number_of_nodes] [number_of_edges]
# [one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
# [one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]
# ...

# For example, the third line of the file is "2 3 -8874", indicating that 
# there is an edge connecting vertex #2 and vertex #3 that has cost -8874.

# You should NOT assume that edge costs are positive, nor should 
# you assume that they are distinct.

# Your task is to run Prim's minimum spanning tree algorithm on this graph. 
# You should report the overall cost of a minimum spanning tree --- 
# an integer, which may or may not be negative --- in the box below.

# IMPLEMENTATION NOTES: This graph is small enough that the 
# straightforward O(mn) time implementation of Prim's algorithm should 
# work fine. OPTIONAL: For those of you seeking an additional challenge, 
# try implementing a heap-based version. The simpler approach, which 
# should already give you a healthy speed-up, is to maintain relevant 
# edges in a heap (with keys = edge costs). The superior approach stores 
# the unprocessed vertices in the heap, as described in lecture. 
# Note this requires a heap that supports deletions, and you'll probably 
# need to maintain some kind of mapping between vertices and their positions 
# in the heap.

# Create a list of integers from txt-file
fh = open("edges.txt", "r") 
list_str = fh.readlines()
fh.close()
#Create a list of dicts for adjacency list representetoin
graph = [{} for i in range(501)]
for line in list_str[1:]:
    node_1 = int(line.split()[0])
    node_2 = int(line.split()[1])
    weight = int(line.split()[2])
    graph[node_1][node_2] = weight
    graph[node_2][node_1] = weight

#Prime's algo
X = [1]
T = 0
H = list(range(2, 501))
while H:
    node_new = 0
    weight_new = 0
    for node in X:
        for edge in graph[node]:
            if edge in H:
                if node_new == 0 or graph[node][edge] < weight_new:
                    node_new = edge
                    weight_new = graph[node][edge]
    T += weight_new
    X += [node_new]
    H.remove(node_new)

answer_ex3 = T            