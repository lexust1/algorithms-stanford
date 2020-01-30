#Very simple Karger's algo implemintation

import random
import copy

# random.seed(0.2)

# find_node_index finds index for every node.
# Input: adj. list, the 1st and 2nd nodes
# Output: tuple with index for every node
def find_node_index(list_adj, node_1, node_2):
    for el in enumerate(list_adj):
        if el[1][0] == node_1:
            node_1_idx = el[0]
            # print('node_1_idx:', node_1_idx)
        if el[1][0] == node_2:
            node_2_idx = el[0]
            # print('node_2_idx:', node_2_idx)
    node_idx = (node_1_idx, node_2_idx)        
    return node_idx

# karger_algo function implements Karger's algorithm for graph.
# Input: adj. list
# Output: number of cuts
def karger_algo(list_adj):
    count = 0
    while len(list_adj) > 2:
        # Find random edge 
        row_adj = random.choice(list_adj)
        # print('row_adj:', row_adj)
        node_1 = row_adj[0]
        # print('node_1:', node_1)
        node_2 = random.choice(row_adj[1:])
        # print('node_2:', node_2)
        # Find indexes for nodes   
        if count == 0: #
            node_1_idx = node_1 - 1
            node_2_idx = node_2 - 1  
            count += 1
        else:
            node_idx = find_node_index(list_adj, node_1, node_2)
            node_1_idx = node_idx[0]
            node_2_idx = node_idx[1]       
        # Add nodes from adj. list row of node_2 to adj. list row of node_1
        # print('list_adj[node_1_idx]:', list_adj[node_1_idx])
        list_adj[node_1_idx].extend(list_adj[node_2_idx])
        # print('list_adj[node_1_idx]:', list_adj[node_1_idx])    
        # Replace node_2 by node_1 in adj. list.
        for i in range(len(list_adj)):
            list_adj[i] = [node_1 if x == node_2 else x for x in list_adj[i]]
        # Delete duplicates of node_1 in node_1 row only!
        list_adj_new = []    
        for el in list_adj[node_1_idx]:
            if el == node_1 and el not in list_adj_new:
                list_adj_new.append(node_1)
            elif el != node_1:
                list_adj_new.append(el)
        list_adj[node_1_idx] = list_adj_new
        # print('list_adj[node_1_idx]:', list_adj[node_1_idx])
        # Delete (contract) node_2
        del list_adj[node_2_idx]
        # print('list_adj:', list_adj)
        # print('================')
    #print('Answer:', len(list_adj[1]) - 1)
    num_cut = len(list_adj[1]) - 1
    return num_cut

# karger_min_cut func. counts the number of minimum cuts 
# Input: ajd. list and number of iterations 
# Output: minimun cut of graph
def karger_min_cut(list_adj, num_iters):
    list_of_cut = []
    for it in range(num_iters):
        list_adj_copy = copy.deepcopy(list_adj)
        list_of_cut.append(karger_algo(list_adj))
        list_adj = list_adj_copy
    return min(list_of_cut)

# Create an adj. list from txt-file
fh = open('kargerMinCut.txt', 'r')
#fh = open('karger_small.txt', 'r')
list_str = fh.readlines()
fh.close()
list_adj = []
for line in list_str:
    list_adj.append([int(el) for el in line.split()])

#Set number of iterations in order to find minimum number of cuts    
min_cut = karger_min_cut(list_adj, 100)
print(min_cut)