# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 15:30:17 2021

@author: Rodrigo
"""

def prob(t,a,n,b,i,j,h):
    
    p = t[i][j]**a * n[i][j] ** b / a
    
    return p