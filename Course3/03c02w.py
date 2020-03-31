# 1. In this programming problem and the next you'll code up the clustering 
# algorithm from lecture for computing a max-spacing kk-clustering.

# Download the text file below.
# clustering1.txt
# This file describes a distance function (equivalently, a complete graph 
# with edge costs). It has the following format:

# [number_of_nodes]
# [edge 1 node 1] [edge 1 node 2] [edge 1 cost]
# [edge 2 node 1] [edge 2 node 2] [edge 2 cost]
# ...

# There is one edge (i,j)(i,j) for each choice of 1≤i<j≤n, where n
#  is the number of nodes.

# For example, the third line of the file is "1 3 5250", indicating that 
# the distance between nodes 1 and 3 (equivalently, the cost 
# of the edge (1,3)) is 5250. You can assume that distances are positive, 
# but you should NOT assume that they are distinct.

# Your task in this problem is to run the clustering algorithm from lecture 
# on this data set, where the target number k of clusters is set to 4. 
# What is the maximum spacing of a 4-clustering?

# ADVICE: If you're not getting the correct answer, try debugging your 
# algorithm using some small test cases. And then post them to 
# the discussion forum!

import copy

# Create a list of integers from txt-file
fh = open("clustering1.txt", "r") 
list_str = fh.readlines()
fh.close()
#Create a list of dicts for adjacency list representetoin
graph = {}
for line in list_str[1:]:
    node_1 = int(line.split()[0])
    node_2 = int(line.split()[1])
    cost = int(line.split()[2])
    graph[(node_1, node_2)] = cost
#Kruskul's algo for clustering.      
G = copy.deepcopy(graph)
clust = list(range(1, 501))
num_clust = 500
for e in graph:
    edge = min(G, key=G.get)
    dist = G.pop(edge)
    vert_1 = clust[edge[0] - 1]
    vert_2 = clust[edge[1] - 1]
    if vert_1 != vert_2 and num_clust > 4:
        num_clust -= 1
        for i in range(500):
            if clust[i] == vert_2: clust[i] = vert_1
    elif vert_1 != vert_2 and num_clust == 4:
        answer_ex1 = dist
        break

# 2. In this question your task is again to run the clustering algorithm 
# from lecture, but on a MUCH bigger graph. So big, in fact, that 
# the distances (i.e., edge costs) are only defined implicitly, 
# rather than being provided as an explicit list.

# The data set is below.

# clustering_big.txt
# The format is:

# [# of nodes] [# of bits for each node's label]
# [first bit of node 1] ... [last bit of node 1]
# [first bit of node 2] ... [last bit of node 2]
# ...

# For example, the third line of the file 
# "0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1" denotes the 24 bits 
# associated with node #2.

# The distance between two nodes u and v in this problem is defined as 
# the Hamming distance --- the number of differing bits --- between the 
# two nodes' labels. For example, the Hamming distance between the 24-bit 
# label of node #2 above and 
# the label "0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1" is 3 
# (since they differ in the 3rd, 7th, and 21st bits).

# The question is: what is the largest value of k such that there is 
# a k-clustering with spacing at least 3? That is, how many clusters 
# are needed to ensure that no pair of nodes with all but 2 bits in common 
# get split into different clusters?

# NOTE: The graph implicitly defined by the data file is so big that you 
# probably can't write it out explicitly, let alone sort the edges by cost. 
# So you will have to be a little creative to complete this part of 
# the question. For example, is there some way you can identify the 
# smallest distances without explicitly looking at every pair of nodes?

# Crete and convert digs        
def create_list_of_digs(digs):
    list_of_digs = []
    for i in range(24): # 24 - num of bytes
        dig = list(digs)
        if dig[i] == '0':
            dig[i] = '1'
        else:
            dig[i] = '0'
        list_of_digs += [int(''.join(dig), 2)]
        
        for j in range(i+1, 24): # 24 - num of bytes
            dig_c = dig.copy()
            if dig_c == '0':
                dig_c[j] = '1'
            else:
                dig_c[j] = '0'
            list_of_digs += [int(''.join(dig_c), 2)]
        #print(list_of_digs)
    return list_of_digs

# Find procedure
def find(el):
    global union_find
    
    if union_find[el] == el:
        return el
    elif union_find[union_find[el]] == union_find[el]:
        return union_find[el]
    else:
        el_new = union_find[el]
        while union_find[el_new] != el_new:
            el_new = union_find[el_new]
        union_find[el] = el_new
        return el_new

# Merge procedure
def merge(el_1, el_2):
    global union_find
    global pos
    el_1 = find(el_1)
    el_2 = find(el_2)
    
    if el_1 != el_2:
        if pos[el_1] > pos[el_2]:
            union_find[el_2] = el_1
        elif pos[el_1] < pos[el_2]:
            union_find[el_1] = el_2
        else:
            union_find[el_2] = el_1
            pos[el_1] += 1

# Create a list of integers from txt-file
fh = open("clustering_big.txt", "r") 
list_str = fh.readlines()
fh.close()
# Clear lines
graph = [line.strip().replace(' ', '') for line in list_str[1:]]
graph = list(set(graph))
# Convert system
G = [int(line, 2) for line in graph]

# UnionFind structure as dict
union_find = {key: key for key in G}
pos = {key: 0 for key in G}

for dig in range(len(graph)):
    for el in create_list_of_digs(graph[dig]):
        if el in union_find:
            merge(G[dig], el)

[find(x) for x in union_find]

answer_ex2 = len(set(union_find.values()))



    
