# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 11:14:29 2021

@author: Rodrigo
"""

def dist(x1,y1,x2,y2):
    
    return abs(x1-x2) + abs(y1+y2)

def binomialCoeff(n, k):
 
    res = 1
 
    # Since C(n, k) = C(n, n-k)
    if (k > n - k):
        k = n - k
 
    # Calculate value of
    # [n * (n-1) *---* (n-k+1)] /
    # [k * (k-1) *---* 1]
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
 
    return res
 
# Function to return the number
# of paths
def countPaths(x1, y1, x2, y2):
 
    # Difference between the 'x'
    # coordinates of the given points
    m = abs(x1 - x2)
 
    # Difference between the 'y'
    # coordinates of the given points
    n = abs(y1 - y2)
 
    return (binomialCoeff(m + n, n))


x1=0
y1=7

x2=1
y2=5

print(dist(x1, y1, x2, y2))

print(countPaths(x1, y1, x2, y2))