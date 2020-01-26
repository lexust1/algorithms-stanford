# GENERAL DIRECTIONS:

# Download the following text file:

# QuickSort.txt
# The file contains all of the integers between 1 and 10,000 (inclusive, 
# with no repeats) in unsorted order. The integer in the i^{th}ith row of 
# the file gives you the i^{th}ith entry of an input array.

# Your task is to compute the total number of comparisons used to sort 
# the given input file by QuickSort. As you know, the number of comparisons 
# depends on which elements are chosen as pivots, so we'll ask you 
# to explore three different pivoting rules.

# You should not count comparisons one-by-one. Rather, when there is 
# a recursive call on a subarray of length mm, you should simply add 
# m-1m−1 to your running total of comparisons. (This is because the pivot 
# element is compared to each of the other m-1m−1 elements in the subarray 
# in this recursive call.)

# WARNING: The Partition subroutine can be implemented in several different 
# ways, and different implementations can give you differing numbers of 
# comparisons. For this problem, you should implement the Partition 
# subroutine exactly as it is described in the video lectures 
# (otherwise you might get the wrong answer).

# DIRECTIONS FOR THIS PROBLEM:

# For the first part of the programming assignment, you should always use 
# the first element of the array as the pivot element.

# HOW TO GIVE US YOUR ANSWER:

# Type the numeric answer in the space provided.

# So if your answer is 1198233847, then just type 1198233847 in the space 
# provided without any space / commas / other punctuation marks. You have 5 
# attempts to get the correct answer.

# (We do not require you to submit your code, so feel free to use the 
# programming language of your choice, just type the numeric answer 
# in the following space.)

# 2.Question 2
# GENERAL DIRECTIONS AND HOW TO GIVE US YOUR ANSWER:

# See the first question.

# DIRECTIONS FOR THIS PROBLEM:

# Compute the number of comparisons (as in Problem 1), always using the final 
# element of the given array as the pivot element. Again, be sure to 
# implement the Partition subroutine exactly as it is described in 
# the video lectures.

# Recall from the lectures that, just before the main Partition subroutine, 
# you should exchange the pivot element (i.e., the last element) with the 
# first element

# 3.Question 3
# GENERAL DIRECTIONS AND HOW TO GIVE US YOUR ANSWER:

# See the first question.

# DIRECTIONS FOR THIS PROBLEM:

# Compute the number of comparisons (as in Problem 1), using the 
# "median-of-three" pivot rule. [The primary motivation behind this rule is 
# to do a little bit of extra work to get much better performance on input 
# arrays that are nearly sorted or reverse sorted.] In more detail, you 
# should choose the pivot as follows. Consider the first, middle, and final 
# elements of the given array. (If the array has odd length it should be 
# clear what the "middle" element is; for an array with even length 2k2k, 
# use the k^{th}kth element as the "middle" element. 

# So for the array 4 5 6 7, the "middle" element is the second one ---- 5 and
# not 6!) Identify which of these three elements is the median (i.e., the one
# whose value is in between the other two), and use this as your pivot. 
# As discussed in the first and second parts of this programming assignment, 
# be sure to implement Partition exactly as described in the video lectures 
# (including exchanging the pivot element with the first element just before 
# the main Partition subroutine).

# EXAMPLE: For the input array 8 2 4 5 7 1 you would consider the first (8), 
# middle (4), and last (1) elements; since 4 is the median of 
# the set {1,4,8}, you would use 4 as your pivot element.

# SUBTLE POINT: A careful analysis would keep track of the comparisons made 
# in identifying the median of the three candidate elements. You should NOT 
# do this. That is, as in the previous two problems, you should simply add 
# m-1m−1 to your running total of comparisons every time you recurse on 
# a subarray with length mm.

# Function partition(A, left, right) find the pivot position and separate 
# an array around the pivot element (every part around the pivot element is
# an array of distinct integers)
# Input: 
# A - an array of distinct integers;
# left and righ - endpoints for array;
# Output:
# i - 1 - final position of pivot element
def partition(A, left, right):
    p = A[left]
    i = left + 1
    j = left + 1
    while j <= right:
        if A[j] < p:
            temp_A_i = A[i]
            A[i] = A[j]
            A[j] = temp_A_i
            i += 1
            j += 1
        else: 
            j += 1
    temp_A_p = A[i - 1]
    A[i - 1] = p
    A[left] = temp_A_p
    return i - 1

# choose_pivot(A, left, right, ch) function helps choose one of three ways to
# work with a pivot element:
#    1 - use the first element as the pivot one;
#    2 - use the last element as the pivot one;
#    3 - ust the median as the pivot element;  
# Input: 
# A - array  of distinct integers;
# left and right - endpoints
# ch - choose what use as the pivot element:
#    'first' - use the first element as the pivot one;
#    'last' - use the last element as the pivot one;
#    'median' - use the median as the pivot element;
# Output: pivot element index
def choose_pivot(A, left, right, ch):
    # The first case: the first element is the pivot one
    if ch == 'first':
        return left
    # The second case: the last element is the pivot one
    if ch == 'last':
        return right
    # The third case: the median is the pivot element
    if ch == 'median':
        # Find index of medium element
        med = left + (right - left)//2
        # Find median
        if ((A[med] >= A[left] and A[med] <= A[right]) or
            (A[med] <= A[left] and A[med] >= A[right])): 
            median = A[med]
        if ((A[left] >= A[med] and A[left] <= A[right]) or
            (A[left] <= A[med] and A[left] >= A[right])): 
            median = A[left]
        if ((A[right] >= A[med] and A[right] <= A[left]) or
            (A[right] <= A[med] and A[right] >= A[left])):
            median = A[right]
        #Swap elements
        if median == A[right]:
            temp_A = A[right]
            A[right] = A[left]
            A[left] = temp_A
        elif median == A[med]:
            temp_A = A[med]
            A[med] = A[left]
            A[left] = temp_A 
        return left 

# Sort elements and count number of comparisions    
# Input:
# A - array  of distinct integers;
# left and right - endpoints
# ch - choose what use as the pivot element:
#    'first' - use the first element as the pivot one;
#    'last' - use the last element as the pivot one;
#    'median' - use the median as the pivot element;
# Output: number of comparisions         
def quick_sort(A, left, right, ch):
    if left >= right:
        return 0
    
    i = choose_pivot(A, left, right, ch)
    temp_p = A[i]
    A[i] = A[left]
    A[left] = temp_p
    j = partition(A, left, right)
    
    comp1 = quick_sort(A, left, j-1, ch)
    comp2 = quick_sort(A, j+1, right, ch)
    return comp1 + comp2 + right - left
  
# Create array from txt-file
fh = open('QuickSort.txt', 'r')
list_str = fh.readlines()
fh.close()
ar = [int(line) for line in list_str]
# Set parameters for assigment         
A = ar
left = 0
right = len(A) - 1
ch = 'median'
comp = quick_sort(A, left, right, ch)
print(comp)
            
            
            
        