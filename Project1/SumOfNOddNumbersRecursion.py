__author__ = 'Rinisha'
__date__ = '10/24/2015'


def sum (n):
    if n==1 :
        return n
    else:
        x= n + n - 1
        return x + sum(n-1)

print(sum(-7))