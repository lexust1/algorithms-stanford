# Download the following text file:
# IntegerArray.txt

# This file contains all of the 100,000 integers between 1 and 100,000 
# (inclusive) in some order, with no integer repeated.

# Your task is to compute the number of inversions in the file given, 
# where the ithi^{th}ith row of the file indicates the ithi^{th}ith entry 
# of an array.

# Because of the large size of this array, you should implement the fast 
# divide-and-conquer algorithm covered in the video lectures.

# The numeric answer for the given input file should be typed 
# in the space below.

# So if your answer is 1198233847, then just type 1198233847 in the space 
# provided without any space / commas / any other punctuation marks. 
# You can make up to 5 attempts, and we'll use the best one for grading.

# (We do not require you to submit your code, so feel free to use 
# any programming language you want --- just type the final numeric answer 
# in the following space.)

# [TIP: before submitting, first test the correctness of your program 
# on some small test files or your own devising. Then post your best test 
# cases to the discussion forums to help your fellow students!]

# Array names are similar to pseudocode in the book.

# Function merge_and_count_split_inv(C, D) merge arrays and count split 
# inversions.
# Input:C and D are sorted arrays
# Output: sorted array B and number of split inversions (B, inv_split)
def merge_and_count_split_inv(C, D): 
    len_C_plus_D = len(C) + len(D)
    
    i = 0
    j = 0
    k = 0
    inv_split = 0
    B = [0]*len_C_plus_D
    while i < len(C) and j < len(D):
        if C[i] < D[j]:
            B[k] = C[i]
            i += 1
        else: # C[i] > D[j], i.e. condition for inversion
            B[k] = D[j]
            # Count split invercions
            inv_split += (len(C) - i) 
            j += 1
        k += 1
        
    while i < len(C):
        B[k] = C[i]
        i += 1
        k += 1
    
    while j < len(D):
        B[k] = D[j]
        j += 1
        k += 1

    return B, inv_split            

# Function sort_and_count_inv(A) sort (divide) arrays and count all types of
# inversions.
# Input: A is an unsorted array
# Output: sorted array B and number of all type of inversions 
# (B, inv_left + inv_right + inv_split)
def sort_and_count_inv(A):
    len_A = len(A)
    if len_A < 2:
        return A, 0
    else:
        C, inv_left = sort_and_count_inv(A[:len_A//2])
        D, inv_right = sort_and_count_inv(A[len_A//2:])
        B, inv_split = merge_and_count_split_inv(C, D)
        return B, inv_left + inv_right + inv_split

# Create array from txt-file
fh = open('IntegerArray.txt', 'r')
list_str = fh.readlines()
fh.close()
ar = [ int(line) for line in list_str]

ar_sort, inv = sort_and_count_inv(ar)

print(inv)