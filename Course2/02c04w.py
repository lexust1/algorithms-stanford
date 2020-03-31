# Download the following text file:

# algo1-programming_prob-2sum.txt

# The goal of this problem is to implement a variant of the 2-SUM algorithm 
# covered in this week's lectures.

# The file contains 1 million integers, both positive and negative 
# (there might be some repetitions!).This is your array of integers, 
# with the i^{th} row of the file specifying the i^{th} ntry of the array.

# Your task is to compute the number of target values tt in 
# the interval [-10000,10000] (inclusive) such that there are distinct 
# numbers x,yx,y in the input file that satisfy x+y=tx+y=t. 
# (NOTE: ensuring distinctness requires a one-line addition to the 
# algorithm from lecture.)

# Write your numeric answer (an integer between 0 and 20001) 
# in the space provided.

# OPTIONAL CHALLENGE: If this problem is too easy for you, try 
# implementing your own hash table for it. For example, you could 
# compare performance under the chaining and open addressing approaches 
# to resolving collisions.

# It's an algorithm from the course but it's very slow!!!
# In fact, it's better to use lists/dicts and bisect library.
# General problem is a too long integers in big array.

# Create a dict of integers from txt-file
with open("algo1-programming_prob-2sum.txt", "r") as fh:
    dic_H = {int(el): None for el in fh}
# Target values
t_ar = range(-10000, 10001)
# Find the num of number of target values
num_t_val = []
for t in t_ar:
    for key in dic_H:
        y = t - key
        if y in dic_H and y != key:
            num_t_val.append((t, key, y))
            #print(num_t_val)
            break

answer = len(num_t_val)             

        
