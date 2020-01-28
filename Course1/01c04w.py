import random

# Create an adj. list from txt-file
fh = open('kargerMinCut.txt', 'r')
list_str = fh.readlines()
fh.close()
list_adj = []
for line in list_str:
    list_adj.append([int(el) for el in line.split()])

while len(list_adj) > 2:
    # Find random edge 
    row_adj = random.choice(list_adj)
    node_1 = row_adj[0]
    node_2 = random.choice(row_adj[1:])
#!!!![node_1 - 1] поменять логику через индексацию (меняется после каждой итерации),
# возможно, есть смысле на стадии random ограничить список элементов - индексов)
# Надо сделать трекинг отдельного листа с node. Удалять в ходе каждой итерации.    
    # Remove node_2 element from node_1 row in adj.list 
    list_adj[node_1 - 1].remove(node_2)
    # Remove node_1 element from node_2 row in adj.list 
    list_adj[node_2 - 1].remove(node_1)
    # Add nodes from adj. list row of node_2 to adj. list row of node_1
    list_adj[node_1 - 1].extend(list_adj[node_2 - 1][1:])
    #Delete (contract) node_2
    del list_adj[node_2 - 1]
    
    #Replace node_2 by node_1 in adj. list.
    for i in range(len(list_adj)):
        list_adj[i] = [node_1 if x == node_2 else x for x in list_adj[i]]
        
#    new = list_adj
    
        
        

    

# # Find random edge 
# row_adj = random.choice(list_adj)
# node_1 = row_adj[0]
# node_2 = random.choice(row_adj)

# # Remove node_2 element from node_1 row in adj.list 
# list_adj[node_1 - 1].remove(node_2)
# # Remove node_1 element from node_2 row in adj.list 
# list_adj[node_2 - 1].remove(node_1)
# # Add nodes from adj. list row of node_2 to adj. list row of node_1
# list_adj[node_1 - 1].extend(list_adj[node_2 - 1][1:])
# #Delete (contract) node_2
# del list_adj[node_2 - 1]

# #Replace node_2 by node_1 in adj. list.
# for i in range(len(list_adj)):
#     list_adj[i] = [node_1 if x == node_2 else x for x in list_adj[i]]
    
# #     count += 1
# #Check list_adj
# for row_adj in list_adj:
#     print(node_2 in row_adj)

#