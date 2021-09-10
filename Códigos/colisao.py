# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 20:10:59 2021

@author: Rodrigo
"""

def col(c1,c2):
    
    n = min(len(c1),len(c2))
    
    for i in range(n):
        
        if c1[i] == c2[i]:
            
            if c1[i+1] == c2[i-1]:
                
                pass
            
            else:
            
                c2.insert(i,c2[i-1])
                
            i=0
                
    return c1,c2
                
                
                
                
c1 = [(1,0),(1,1),(1,2)]

c2 = [(0,1),(1,1),(2,1)]

c3,c4 = col(c1,c2)