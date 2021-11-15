"""Python program to find sum of
multiples of a number up to N"""
 
# Calculates sum of multiples of
# a number upto N
def calculate_sum(a, N):
 
    # Number of multiples
    m = N / a
 
    # sum of first m natural numbers
    sum = m * (m + 1) / 2
 
    # sum of multiples
    ans = a * sum
 
    print("Sum of multiples of ", a,
          " up to ", N, " = ", ans)
 
# Driver Code
calculate_sum(7, 49)