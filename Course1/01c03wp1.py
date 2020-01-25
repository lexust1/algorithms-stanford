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
            
A = [3, 8, 2, 5, 1, 4, 7, 6]
left = 0
right = len(A) - 1
            
            
            
        