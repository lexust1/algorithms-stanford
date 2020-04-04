# 1.Question 1
# In this assignment you will implement one or more algorithms for the 2SAT 
# problem. Here are 6 different 2SAT instances:

# 2sat1.txt
# 2sat2.txt
# 2sat3.txt
# 2sat4.txt
# 2sat5.txt
# 2sat6.txt

# The file format is as follows. In each instance, the number of variables 
# and the number of clauses is the same, and this number is specified on the 
# first line of the file. Each subsequent line specifies a clause via its 
# two literals, with a number denoting the variable and a "-" sign denoting 
# logical "not". For example, the second line of the first data file 
# is "-16808 75250", which indicates the clause ¬x16808∨x75250.

# Your task is to determine which of the 6 instances are satisfiable, and 
# which are unsatisfiable. In the box below, enter a 6-bit string, where 
# the ith bit should be 1 if the ith instance is satisfiable, and 0 
# otherwise. 
# For example, if you think that the first 3 instances are satisfiable and 
# the last 3 are not, then you should enter the string 111000 
# in the box below.

# DISCUSSION: This assignment is deliberately open-ended, and you can 
# implement whichever 2SAT algorithm you want. For example, 2SAT reduces 
# to computing the strongly connected components of a suitable graph 
# (with two vertices per variable and two directed edges per clause, 
# you should think through the details). This might be an especially 
# attractive option for those of you who coded up an SCC algorithm in Part 2 
# of this specialization. Alternatively, you can use Papadimitriou's 
# randomized local search algorithm. (The algorithm from lecture is probably 
# too slow as stated, so you might want to make one or more simple 
# modifications to it --- even if this means breaking the analysis given in 
# lecture --- to ensure that it runs in a reasonable amount of time.) 
# A third approach is via backtracking. In lecture we mentioned this approach
# only in passing; see Chapter 9 of the Dasgupta-Papadimitriou-Vazirani book, 
# for example, for more details.

import numpy as np

# Create graphs form txt-file
def create_graphs(name):
    cl = np.loadtxt(name, skiprows=1, dtype=int)
    c1 = cl[:, 0]
    c2 = cl[:, 1]
    
    n = np.loadtxt(name, max_rows=1, dtype=int)
    
    G = {k: [] for k in range(- n, n + 1) if k != 0}
    Gr = {k: [] for k in range(- n, n + 1) if k != 0}
    for idx in range(n):
        G[-c1[idx]].append(c2[idx])
        G[-c2[idx]].append(c1[idx])
        Gr[c1[idx]].append(-c2[idx])
        Gr[c2[idx]].append(-c1[idx]) 
    return G, Gr, n

# DFS
def dfs(graph, i):
    global time, fin_time, s, expl, leader
    for j in graph[i]:
        if not expl[j]:
            expl[j] = True
            leader[j] = s
            return j
    time += 1
    if time == 0:
        time += 1
    fin_time[i] = time
    return 0

# DFS for ev. loop
def dfs_loop(graph):
    global time, fin_time, s, expl
    for i in reversed(list(graph.keys())):
        if not expl[i]:
            s = i
            expl[i] = True
            leader[i] = s
            expl_lst = [i]
            while expl_lst:
                j = dfs(graph, expl_lst[-1])
                if j == 0:
                    expl_lst.pop(-1)
                else:
                    expl_lst.append(j)

def find_ans(G, Gr, n):
    global time, s, fin_time, leader, m, expl
    # First loop
    time = - n - 1
    s = None
    expl = {i: False for i in G}
    fin_time = {i: 0 for i in G}
    leader = {i: 0 for i in G}
    dfs_loop(Gr)
    
    Gnew = {node: [] for node in G}
    for node in G:
        {Gnew[fin_time[node]].append(fin_time[el]) for el in G[node]}
    fin_time_r = {fin_time[i]: i for i in G}
    
    #Second loop
    time = - n - 1
    m = 0
    expl = {i: False for i in G}
    fin_time = {i: 0 for i in G}
    leader = {i: 0 for i in G}
    dfs_loop(Gnew)
    
    #SCC and 2SAT
    scc = {}
    for i in leader:
        if leader[i] in scc:
            scc[leader[i]] += [fin_time_r[i]]
        else:
            scc[leader[i]] = [fin_time_r[i]]
    
    cnt = 0
    fl = None
    for i in scc:
        if len(scc[i]) > 1:
            cnt += 1
            for j in scc[i]:
                if -j in scc[i]:
                    fl = False
                    print('False')
                    break
    if fl is None: 
        fl = True
        print('True')
    return fl
# Start algo and construct answer
name_lst = ["2sat1.txt", "2sat2.txt", "2sat3.txt", 
            "2sat4.txt", "2sat5.txt", "2sat6.txt"]
answer_ex = ''

for name in name_lst:
    G, Gr, n = create_graphs(name)
    fl = find_ans(G, Gr, n)
    if fl is False: 
        answer_ex += '0'
    else: #fl is True
        answer_ex += '1'

print('Final answer:', answer_ex)
