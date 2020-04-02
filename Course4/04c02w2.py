# In this assignment you will implement one or more algorithms for 
# the traveling salesman problem, such as the dynamic programming algorithm 
# covered in the video lectures. Here is a data file describing 
# a TSP instance.

# tsp.txt
# The first line indicates the number of cities. Each city is a point in 
# the plane, and each subsequent line indicates the x- and y-coordinates 
# of a single city.

# The distance between two cities is defined as the Euclidean distance --- 
# that is, two cities at locations (x,y)(x,y) and (z,w)(z,w) have 
# distance sqrt{(x-z)^2 + (y-w)^2} between them.

# In the box below, type in the minimum cost of a traveling salesman tour 
# for this instance, rounded down to the nearest integer.

# OPTIONAL: If you want bigger data sets to play with, check out 
# the TSP instances from around the world here. The smallest data 
# set (Western Sahara) has 29 cities, and most of the data sets are much 
# bigger than that. What's the largest of these data sets that you're able 
# to solve --- using dynamic programming or, if you like, a completely 
# different method?

# HINT: You might experiment with ways to reduce the data set size. 
# For example, trying plotting the points. Can you infer any structure of 
# the optimal solution? Can you use that structure to speed up your 
# algorithm? 


# You can use the hint from assignment and to plot all cities. Then you can 
# see it is possible to divide all 25 cities to clusters 12 and 13 cities. 
# Then you use algo from the lecture for every cluster and add result of 
# two clusters (it’s too long to use algo for all 25 cities). And correct 
# answer 26442. 

# At the same time, I’m not sure it’s the best way and the correct answer.

# You can use MST and DFS for Euclidian TSP. It’s very fast and give a 
# shorter path. MST and DFS can be used from previous lectures or from 
# networkx-library and then the correct answer is 24895. Therefore I’ve kept 
# this code version.

import numpy as np
import networkx as nx


x_y = np.loadtxt("tsp.txt", skiprows=1)
x = x_y[:, 0]
y = x_y[:, 1]

n = 25
graph = {i: {} for i in range(n + 1)}
G = nx.Graph()
for node_1 in range(n):
    for node_2 in range(n):
        if node_1 != node_2:
            dist_sq = np.sqrt((x[node_1] - x[node_2]) ** 2 + (y[node_1] - y[node_2]) ** 2)
            graph[node_1 + 1][node_2 + 1] = dist_sq
            graph[node_2 + 1][node_1 + 1] = dist_sq
            G.add_edge(node_1 + 1, node_2 + 1, weight=dist_sq)
G_MST = nx.minimum_spanning_tree(G, weight = 'weight')
G_DFS = nx.dfs_tree(G_MST, 1) 
TSP = 0
for edge in list(G_DFS.edges()):
    print(edge[0], edge[1])
    # print(graph[edge[0]][edge[1]])
    TSP += graph[edge[0]][edge[1]]
    print(TSP)
answer = TSP + graph[1][3]

