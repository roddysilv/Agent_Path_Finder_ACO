# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 10:17:39 2021

@author: Rodrigo
"""
import numpy as np

def abreInstancia(instancia):
    
    f = open(instancia)
    
    f = f.readlines()
    
    h = int(f[0])
    
    w = int(f[1])
    
    aux=[]
    G=[]
        
    for i in range(w):
        aux.append(0)
    for i in range(h):
        G.append(aux.copy())
    
    for i in range(2,h+2):
    
        for j in range(w):
             G[i-2][j] = f[i][j]
    
    return np.array(G), h, w

def gera(G,h,w,n):
    
    L=[]
    
    for i in range(10):
    
        objetivo = []
    
        while len(objetivo)<n:
        
            x = np.random.randint(1,w)
        
            y = np.random.randint(1,h)
        
            if (x,y) not in objetivo and G[x][y] != "T" :
            
                objetivo.append((x,y))
                
        L.append(objetivo.copy())
    
    return L

I = "../Instâncias/Mapas/M_30x30.txt"

x = I.split('/')

n = 10

G, h, w = abreInstancia(I)

L = np.array(gera(G,h,w,n))

arquivo = open(f'../Instâncias/Tour/{n} buscas/Tour_{x[3]}','w')
for i in range(len(L)):
    for j in range(len(L[0])):
        for k in range (len(L[0][0])):
            arquivo.write(str(L[i][j][k])+' ')
    arquivo.write("\n")

arquivo.close()
