# Programming Assignment #1 (Week 1)
# Greedy algorithm (weight - length) and weight/length ratio
# Prim's minimum spanning tree algorithm

1. In this programming problem and the next you'll code up the greedy algorithms from lecture for minimizing the weighted sum of completion times..

Download the text file below.

jobs.txt
This file describes a set of jobs with positive and integral weights and lengths. It has the format

[number_of_jobs]

[job_1_weight] [job_1_length]

[job_2_weight] [job_2_length]

...

For example, the third line of the file is "74 59", indicating that the second job has weight 74 and length 59.

You should NOT assume that edge weights or lengths are distinct.

Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing order of the difference (weight - length). Recall from lecture that this algorithm is not always optimal. IMPORTANT: if two jobs have equal difference (weight - length), you should schedule the job with higher weight first. Beware: if you break ties in a different way, you are likely to get the wrong answer. You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below.

ADVICE: If you get the wrong answer, try out some small test cases to debug your algorithm (and post your test cases to the discussion forum).

2. For this problem, use the same data set as in the previous problem.

Your task now is to run the greedy algorithm that schedules jobs (optimally) in decreasing order of the ratio (weight/length). In this algorithm, it does not matter how you break ties. You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below.

3. In this programming problem you'll code up Prim's minimum spanning tree algorithm.

Download the text file below.

edges.txt
This file describes an undirected graph with integer edge costs. It has the format

[number_of_nodes] [number_of_edges]

[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]

[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]

...

For example, the third line of the file is "2 3 -8874", indicating that there is an edge connecting vertex #2 and vertex #3 that has cost -8874.

You should NOT assume that edge costs are positive, nor should you assume that they are distinct.

Your task is to run Prim's minimum spanning tree algorithm on this graph. You should report the overall cost of a minimum spanning tree --- an integer, which may or may not be negative --- in the box below.


# Programming Assignment #2 (Week 2)
# k-clustering (by Kruskul's algo)

1. In this programming problem and the next you'll code up the clustering algorithm from lecture for computing a max-spacing k-clustering.

Download the text file below.

clustering1.txt
This file describes a distance function (equivalently, a complete graph with edge costs). It has the following format:

[number_of_nodes]

[edge 1 node 1] [edge 1 node 2] [edge 1 cost]

[edge 2 node 1] [edge 2 node 2] [edge 2 cost]

...

There is one edge (i,j)(i,j) for each choice of 1≤i<j≤n, where nn is the number of nodes.

For example, the third line of the file is "1 3 5250", indicating that the distance between nodes 1 and 3 (equivalently, the cost of the edge (1,3)) is 5250. You can assume that distances are positive, but you should NOT assume that they are distinct.

Your task in this problem is to run the clustering algorithm from lecture on this data set, where the target number kk of clusters is set to 4. What is the maximum spacing of a 4-clustering?

ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!

Enter answer here
1 point

2.Question 2
In this question your task is again to run the clustering algorithm from lecture, but on a MUCH bigger graph. So big, in fact, that the distances (i.e., edge costs) are only defined implicitly, rather than being provided as an explicit list.

The data set is below.

clustering_big.txt
The format is:

[# of nodes] [# of bits for each node's label]

[first bit of node 1] ... [last bit of node 1]

[first bit of node 2] ... [last bit of node 2]

...

For example, the third line of the file "0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1" denotes the 24 bits associated with node #2.

The distance between two nodes uu and vv in this problem is defined as the Hamming distance--- the number of differing bits --- between the two nodes' labels. For example, the Hamming distance between the 24-bit label of node #2 above and the label "0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1" is 3 (since they differ in the 3rd, 7th, and 21st bits).

The question is: what is the largest value of kk such that there is a kk-clustering with spacing at least 3? That is, how many clusters are needed to ensure that no pair of nodes with all but 2 bits in common get split into different clusters?

NOTE: The graph implicitly defined by the data file is so big that you probably can't write it out explicitly, let alone sort the edges by cost. So you will have to be a little creative to complete this part of the question. For example, is there some way you can identify the smallest distances without explicitly looking at every pair of nodes?
