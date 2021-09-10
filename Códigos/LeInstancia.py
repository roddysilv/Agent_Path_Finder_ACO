# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 11:13:22 2021

@author: Rodrigo
"""

import numpy as np

f = open('warehouse-10-20-10-2-1.map/warehouse-10-20-10-2-1.map')

f = f.readlines()

h = f[1]

h = int(h.split()[1])

w = f[2]

w = int(w.split()[1])

A = np.zeros((h,w))

t=[]

for i in range(4,len(f)):
    
    t.append( f[i])
    
for i in range(h):
    
    for j in range(w):
        
        if t[i][j] == '.':
        
            A[i][j] = 1
            
pontos = h*w

def make_matrix(rows, cols):
    n = rows*cols
    M = np.zeros((n,n))
    for r in range(rows):
        for c in range(cols):
            i = r*cols + c
            # Two inner diagonals
            if c > 0: M[i-1,i] = M[i,i-1] = 1
            # Two outer diagonals
            if r > 0: M[i-cols,i] = M[i,i-cols] = 1
    return M

def coord(h,w):
    
    C = np.zeros((w*h,3))
    
    for i in range(w*h):
        
        for j in range(2):
            
            C[i][j] = 0

M=make_matrix(3, 3)

for i in range(h):
    
    for j in range(w):
        
        if t[i][j] == "T":
            
            if i - 1 >=0:
                
                M[i-1][j] = 0
                
            if i+1 < h:
                
                M[i+1][j] = 0
                
            if j - 1 >=0:
                
                M[i][j-1] = 0
                
            if j+1 < w:    
                
                M[i][j+1] = 0