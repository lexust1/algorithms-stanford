# In this programming problem you'll code up Dijkstra's shortest-path 
# algorithm.

# Download the following text file:

# dijkstraData.txt
# The file contains an adjacency list representation of an undirected 
# weighted graph with 200 vertices labeled 1 to 200. Each row consists of 
# the node tuples that are adjacent to that particular vertex along with 
# the length of that edge. For example, the 6th row has 6 as the first entry 
# indicating that this row corresponds to the vertex labeled 6. The next 
# entry of this row "141,8200" indicates that there is an edge between 
# vertex 6 and vertex 141 that has length 8200. The rest of the pairs of 
# this row indicate the other vertices adjacent to vertex 6 and the lengths 
# of the corresponding edges.

# Your task is to run Dijkstra's shortest-path algorithm on this graph, 
# using 1 (the first vertex) as the source vertex, and to compute the 
# shortest-path distances between 1 and every other vertex of the graph. 
# If there is no path between a vertex vv and vertex 1, we'll define the 
# shortest-path distance between 1 and vv to be 1000000.

# You should report the shortest-path distances to the following ten 
# vertices, in order: 7,37,59,82,99,115,133,165,188,197. You should encode 
# the distances as a comma-separated string of integers. So if you find that 
# all ten of these vertices except 115 are at distance 1000 away from 
# vertex 1 and 115 is 2000 distance away, then your answer should 
# be 1000,1000,1000,1000,1000,2000,1000,1000,1000,1000. Remember the order 
# of reporting DOES MATTER, and the string should be in the same order 
# in which the above ten vertices are given. The string should not contain 
# any spaces. Please type your answer in the space provided.

# IMPLEMENTATION NOTES: This graph is small enough that the straightforward 
# O(mn)O(mn) time implementation of Dijkstra's algorithm should work fine. 
# OPTIONAL: For those of you seeking an additional challenge, 
# try implementing the heap-based version. Note this requires a heap 
# that supports deletions, and you'll probably need to maintain some kind 
# of mapping between vertices and their positions in the heap.

# It's an slow dijkstra algorithm (without heap) - big-O(m*n)

import re

# create_graph - create graph
# input: 
# - name of txt-file as a string
# - num_nodes is number of nodes
# output:
# graph, where:
# - index of list is a output node$
# - value of list is a list of tuples, every tuples has a number of 
# input node and length of the edge between output node and input node

def create_graph(name, num_nodes):
    
    graph = [None] * (num_nodes + 1)
    fh = open(name, "r") 
    list_str = fh.readlines()
    fh.close()
    
    for line in list_str:
        line_lst = re.split(',|\t', line.strip())
        line_int = [int(el) for el in line_lst]
        list_of_tuples = []
        for idx in range(1, len(line_int), 2):
            list_of_tuples.append(tuple(line_int[idx:idx + 2]))
        graph[int(line_int[0])] = list_of_tuples
    return graph

name = 'dijkstraData.txt'
num_nodes = 200

# name = 'test2.txt'
# num_nodes = 4
graph = create_graph(name, num_nodes)

# dijkstra algorihtm 
# In the first step X_arr has 1st node
X_arr = [1] 
# In the first step Y_arr has all nodes except the 1st node
Y_arr = list(range(2, num_nodes + 1)) 
s = (1, 0)
# dictionary  - key is explored node and  value is the shortest distance
node_dist_dict = {1: 0}

while Y_arr:
    w_dist_lst = []
    for node_X in X_arr:
        for node_Y in graph[node_X]:
            if node_Y[0] not in node_dist_dict:
                w_dist_lst.append((node_Y[0], node_dist_dict[node_X] 
                                   + node_Y[1]))
    short_edge = min(w_dist_lst, key = lambda x: x[1])
    node_dist_dict[short_edge[0]] = short_edge[1]
    X_arr.append(short_edge[0])
    Y_arr.remove(short_edge[0])

#Create answer
list_of_nodes = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
answer_list = []
for node in list_of_nodes:
    if node in node_dist_dict:
        answer_list.append(node_dist_dict[node])
    else:
        answer_list.append(1000000)
print(answer_list)
        
    

