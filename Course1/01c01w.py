# In this programming assignment you will implement one or more of the integer
#  multiplication algorithms described in lecture.

# To get the most out of this assignment, your program should restrict itself
#  to multiplying only pairs of single-digit numbers. You can implement 
#  the grade-school algorithm if you want, but to get the most out of 
#  the assignment you'll want to implement recursive integer multiplication 
#  and/or Karatsuba's algorithm.

# So: what's the product of the following two 64-digit numbers?

# 3141592653589793238462643383279502884197169399375105820974944592

# 2718281828459045235360287471352662497757247093699959574966967627

# [TIP: before submitting, first test the correctness of your program on some 
#  small test cases of your own devising. Then post your best test cases to 
#  the discussion forums to help your fellow students!]

# [Food for thought: the number of digits in each input number is a 
# power of 2. 
#  Does this make your life easier? Does it depend on which algorithm 
#  you're implementing?]

# The numeric answer should be typed in the space below. So if your answer is 
# 1198233847, then just type 1198233847 in the space provided without 
# any space / commas / any other punctuation marks.

# (We do not require you to submit your code, so feel free to use any 
#  programming language you want --- just type the final numeric answer 
#  in the following space.)
# 1234*5678
# Out[1]: 7006652


num1 = str(3141592653589793238462643383279502884197169399375105820974944592)
num2 = str(2718281828459045235360287471352662497757247093699959574966967627)

def karat_mult(num1, num2):
    len_num1 = len(num1)
    len_num2 = len(num2)
    len_digs1 = len_num1//2 #'//' helps work with odd numbers
    len_digs2 = len_num2//2

    digs1_1 = num1[:len_digs1]
    digs1_2 = num1[len_digs1:]
    digs2_1 = num2[:len_digs2]
    digs2_2 = num2[len_digs2:]    

    if (len(digs1_1) == 1 or
        len(digs1_2) == 1 or
        len(digs2_1) == 1 or
        len(digs2_2) == 1): #look for the shortest algo's branch
        prod1 = str(int(digs1_1)*int(digs2_1))
        prod2 = str(int(digs1_1)*int(digs2_2)) 
        prod3 = str(int(digs1_2)*int(digs2_1))
        prod4 = str(int(digs1_2)*int(digs2_2))
    else:
        prod1 = karat_mult(digs1_1, digs2_1)
        prod2 = karat_mult(digs1_1, digs2_2)
        prod3 = karat_mult(digs1_2, digs2_1)
        prod4 = karat_mult(digs1_2, digs2_2)
    return str(
        int(prod1)*int(10**(len(digs1_1)*2))+
        (int(prod2)+int(prod3))*int(10**len(digs1_1))+ #Karatsuba + Gaus
        int(prod4)
        )

res = karat_mult(num1, num2)

#Check the answer
a = (3141592653589793238462643383279502884197169399375105820974944592 * 
     2718281828459045235360287471352662497757247093699959574966967627)