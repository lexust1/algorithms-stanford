# Download the following text file:

# Median.txt
# The goal of this problem is to implement the "Median Maintenance" algorithm
# (covered in the Week 3 lecture on heap applications). The text file  
# contains a list of the integers from 1 to 10000 in unsorted order; 
# you should treat this as a stream of numbers, arriving one by one. 
# Letting x_i​	  denote the i-th number of the file, the k-th median m_k
# ​is defined as the median of the numbers x_1,...,x_k. 
# (So, if k is odd, then m_k is ((k+1)/2)-th smallest number among
# x_1,...,x_k; if k is even, then m_k is the (k/2)-th smallest number among
# x_1,...,x_k.

# In the box below you should type the sum of these 10000 medians, 
# modulo 10000 (i.e., only the last 4 digits). That is, you should 
# compute (m1+m2+m3+⋯+m10000)mod 10000.

# OPTIONAL EXERCISE: Compare the performance achieved by heap-based and 
# search-tree-based implementations of the algorithm.

import heapq
# Create a list of integers from txt-file
fh = open("Median.txt", "r") 
list_str = fh.readlines()
fh.close()
lst = [int(el) for el in list_str]
# Create empty lists for two heaps and all medians
heap_low = [] #[1, 2 , 3]
heap_high = [] #[5, 6, 7]
medians = [] # 4
# Convert lists to heaps.
heapq.heapify(heap_low)
heapq.heapify(heap_high)
# Add initial conditions 
heap_high.append(lst[0]) # use 2nd heap because heapq has min-heap only
medians.append(lst[0])
# Get every element in list and create algorithm for every heap.
for num in lst[1:]:
    if num > heap_high[0]:
        heapq.heappush(heap_high, num)
    else:
        # Heapq library in python does not have max-heap. Because we need to 
        # use a trick with negative values of min-heap. 
        heapq.heappush(heap_low, -num) #minus num! ()
        
    # Count difference between heaps for balance
    dif_heaps = len(heap_high) - len(heap_low)
    # Choose heap for balance
    if dif_heaps > 1:
        bal_el = heapq.heappop(heap_high)
        heapq.heappush(heap_low, -bal_el) #minus bal_el!
    elif dif_heaps < - 1:
        bal_el = heapq.heappop(heap_low)
        heapq.heappush(heap_high, -bal_el) #minus bal_el!
        
    #Count medians
    if len(heap_low) < len(heap_high):
        medians.append(heap_high[0])
    else:
        medians.append(-heap_low[0])

#Create answer
answer = sum(medians) % 10000

            

            
        
        
    



















