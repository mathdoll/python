__author__ = 'Rinisha'
__date__ = '10/24/2015'

def sum_of_odd (n):

    sum = 0;

    for i in  range(1, n+1):
        nthOdd = 2*i - 1
        sum = sum + nthOdd

    print sum


sum_of_odd(5)