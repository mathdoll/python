
__author__ = 'Rinisha'
__date__ = '11/7/2015'
def fibbinocci_Recursion (n):
    if n <= 1:
        return n
    else:
        return fibbinocci_Recursion(n-1) + fibbinocci_Recursion(n-2)

print fibbinocci_Recursion(7)