# 1. In this programming problem and the next you'll code up the greedy 
# algorithm from the lectures on Huffman coding.

# Download the text file below.

# huffman.txt
# This file describes an instance of the problem. It has the following format:

# [number_of_symbols]
# [weight of symbol #1]
# [weight of symbol #2]
# ...

# For example, the third line of the file is "6852892," indicating that 
# the weight of the second symbol of the alphabet is 6852892. (We're using 
# weights instead of frequencies, like in the "A More Complex Example" video.)

# Your task in this problem is to run the Huffman coding algorithm from 
# lecture on this data set. What is the maximum length of a codeword in 
# the resulting Huffman code?

# ADVICE: If you're not getting the correct answer, try debugging your 
# algorithm using some small test cases. And then post them to 
# the discussion forum!

# Create a list of integers from txt-file
fh = open("huffman.txt", "r") 
list_str = fh.readlines()
fh.close()
weights = [int(line.strip()) for line in list_str[1:]]
# Symbols from book
F = {idx: weights[idx] for idx in range(1000)}
P = [[num] for num in range(1000)]
idx_T_3 = 1000
while len(F) > 2:
    # Find two mins and remove from F
    idx_T_1 = min(F, key=F.get)
    T_1 = F.pop(idx_T_1)
    idx_T_2 = min(F, key=F.get)
    T_2 = F.pop(idx_T_2)
    # Merge T1 and T2 and to F
    T_3 = T_1 + T_2
    F[idx_T_3] = T_3
    idx_T_3 += 1
    P.append(P[idx_T_1] + P[idx_T_2])

#Counts syms
digs = 1000 * [0]
for p in P:
    for sym in p:
        digs[sym] += 1
#Answer for ex1 (max length)
answer_ex1 = max(digs)

# 2. Continuing the previous problem, what is the minimum length of 
# a codeword in your Huffman code?
#Answer for ex2 (min length)
answer_ex2 = min(digs)

# 3. In this programming problem you'll code up the dynamic programming 
# algorithm for computing a maximum-weight independent set of a path graph.

# Download the text file below.
# mwis.txt
# This file describes the weights of the vertices in a path graph (with 
# the weights listed in the order in which vertices appear in the path). 
# It has the following format:

# [number_of_vertices]
# [weight of first vertex]
# [weight of second vertex]
# ...

# For example, the third line of the file is "6395702," indicating that 
# the weight of the second vertex of the graph is 6395702.

# Your task in this problem is to run the dynamic programming algorithm 
# (and the reconstruction procedure) from lecture on this data set. 

# The question is: of the vertices 1, 2, 3, 4, 17, 117, 517, and 997, which
# ones belong to the maximum-weight independent set? (By "vertex 1" we mean 
# the first vertex of the graph---there is no vertex 0.) In the box below, 
# enter a 8-bit string, where the ith bit should be 1 if the ith of these 8 
# vertices is in the maximum-weight independent set, and 0 otherwise. 
# For example, if you think that the vertices 1, 4, 17, and 517 are in 
# the maximum-weight independent set and the other four vertices are not, 
# then you should enter the string 10011010 in the box below.
# Create a list of integers from txt-file

fh = open("mwis.txt", "r") 
list_str = fh.readlines()
fh.close()
w = [int(line.strip()) for line in list_str[1:]]
verts = [[] for idx  in range(1000 + 1)]
A = (1000 + 1) * [0]
A[1] = w[0]
verts[1] = [1]
for idx in range(2, 1001):
    case_1 = A[idx - 1]
    case_2 = A[idx - 2] + w[idx - 1]
    A[idx] = max(case_1, case_2)
    if case_1 > case_2:
        verts[idx] = verts[idx - 1].copy()
    else:
        verts[idx] = verts[idx - 2] + [idx]

# Construct answer
verts_q = [1, 2, 3, 4, 17, 117, 517, 997]
ar = verts[-1]

answer_ex3 = str()
for el in verts_q:
        if el in ar:
            answer_ex3 += '1'
        else:
            answer_ex3 += '0'
            





    
    

