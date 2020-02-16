# The file contains the edges of a directed graph. Vertices are labeled 
# as positive integers from 1 to 875714. Every row indicates an edge, 
# the vertex label in first column is the tail and the vertex label 
# in second column is the head (recall the graph is directed, and the edges 
# are directed from the first column vertex to the second column vertex). 
# So for example, the 11^{th}11th row looks liks : "2 47646". This just 
# means that the vertex with label 2 has an outgoing edge to the vertex 
# with label 47646

# Your task is to code up the algorithm from the video lectures for 
# computing strongly connected components (SCCs), and to run this algorithm 
# on the given graph.

# Output Format: You should output the sizes of the 5 largest SCCs in the 
# given graph, in decreasing order of sizes, separated by commas 
# (avoid any spaces). So if your algorithm computes the sizes of the five 
# largest SCCs to be 500, 400, 300, 200 and 100, then your answer should 
# be "500,400,300,200,100" (without the quotes). If your algorithm finds 
# less than 5 SCCs, then write 0 for the remaining terms. Thus, if your 
# algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then 
# your answer should be "400,300,100,0,0" (without the quotes). 
# (Note also that your answer should not have any spaces in it.)

# WARNING: This is the most challenging programming assignment of 
# the course. Because of the size of the graph you may have to manage 
# memory carefully. The best way to do this depends on your programming 
# language and environment, and we strongly suggest that you exchange tips 
# for doing this on the discussion forums.

# We're going to use an iterative implementation because of python is not 
# optimized for an recursive method.

#Number of nodes in graph
num_nodes = 875714

#Create a list of lists for adjacency list representetoin
graph = [[] for i in range(num_nodes+1)]
graph_rev = [[] for i in range(num_nodes+1)]

# Import the graph from txt-file to adjacency list representation:
# - node_1 is an index list 
# - node_2 is an element in list
fh = open("SCC.txt", "r") 
#fh = open("testSCC.txt", "r") 
#fh = open("test2.txt", "r") 
list_str = fh.readlines()
fh.close()
for line in list_str:
    node_1 = int(line.split()[0])
    node_2 = int(line.split()[1])
    graph[node_1] += [node_2]
    graph_rev[node_2] += [node_1]

# Iterative DFS on reverse graph
# First pass of depth-first search
# (computes f(v)’s, the 'magical' ordering)
stack = []
order_nodes = []
# Mark all vertices as unexplored
explored_nodes = [False] * (num_nodes + 1)
explored_nodes[0] = True
# Create additional dict and list because of iterarive method instead 
# of recursive one
# Use dict for fast work
finish_time_dic = {}
time = 0

for node in range(num_nodes + 1):
    stack.append(node)
    while stack:
        v = stack.pop()
        if explored_nodes[v] is False:
            explored_nodes[v] = True
            stack.append(v) #vertex is finished when we meet it the 2nd time.
            for w in graph_rev[v]:
                if explored_nodes[w] is False:
                    stack.append(w)
        else: # explored_nodes[v] is True: 
            if v not in finish_time_dic:
                finish_time_dic[v] = time
                time += 1

# Iterative DFS on original graph
# Second pass of depth-first search
# (finds SCCs in reverse topological order)        
# Mark all vertices as unexplored
explored_nodes = [False] * (num_nodes + 1)
explored_nodes[0] = True
# The nodes should be visited in reverse order (finishing times)
order_nodes = list(finish_time_dic.keys())
order_nodes.reverse()
# Number of strond connected components
SCC = [0] * (num_nodes + 1)
size_SCC = []            

for node in order_nodes: #finish_time
    count_size_SCC = 0
    stack.append(node)
    while stack:
        v = stack.pop()
        if explored_nodes[v] is False:
            explored_nodes[v] = True
            count_size_SCC += 1
            for w in graph[v]:
                stack.append(w)
    size_SCC.append(count_size_SCC)
    
size_SCC.sort(reverse = True)
print(size_SCC[:5])