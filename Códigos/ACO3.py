# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 10:00:07 2021

@author: rodri
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import choice
import time as t
import datetime as dt
from matplotlib.collections import LineCollection

def D(x,y,objetivos):
    
    d = []
    
    for i in range(len(objetivos)):
        
        d.append(dis(x, y, objetivos[i][0], objetivos[i][1]))
        
    if min(d) == 0:
        
        return 1
    else:
        
        return 1 / min(d)

def dis(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

def getSize(ins):
    f = open(ins)
    
    f = f.readlines()
    
    h = int(f[0])
    
    w = int(f[1])
    
    return h,w

def instancia(ins):
    
    f = open(ins)
    
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
    
    return np.array(G)


def plot(C,obj,n):
    
    h,w=getSize(n)
    
    plt.figure(figsize=(10,10))
    
    x, y = np.meshgrid(np.linspace(0,h-1, h), np.linspace(0, w-1, w))

    plt.plot(x, y,'grey') 

    plt.plot(np.transpose(x), np.transpose(y),'grey') # add this here
    
    
    x = [i[0] for i in C]
    y = [i[1] for i in C]

    plt.plot(x,y,'ko-')
        
    for j in range(len(C)):
        if C[j] in obj:
            plt.annotate(C[j],(x[j],y[j]),color='r')
            
    x=np.array(x)
    y=np.array(y)        
    
    plt.quiver(x[:-1], y[:-1], x[1:]-x[:-1], y[1:]-y[:-1], scale_units='xy', angles='xy', scale=1)
    
    G = instancia(n)
    
    for i in range(h):
        for j in range(w):
            if G[i][j] == "T":
                plt.plot(i,j,'ro')
    
    plt.savefig(f"../Imagens/G{h}x{w}_Obj{len(obj)}.svg",bbox_inches='tight')
    plt.savefig(f"../Imagens/G{h}x{w}_Obj{len(obj)}.png",bbox_inches='tight',dpi=400)

def iniciaFer(h,w):
    
    T = np.zeros((h,w,h,w))
    
    for i in range(h):
        for j in range(w):
            for k in range(h):
                for l in range(w):
                    T[i,j,k,l] = 0.1
    return T

def atualizaFerormonio(caminhos,T,C):
       
    for i in range(len(caminhos)):
        
        for j in range(len(caminhos[i])-1):
            
            old = caminhos[i][j] 
            new = caminhos[i][j+1] 
                                   
            T[old[0], old[1], new[0], new[1]] += C
    
    return T

def grid(h,w):
    
    L1=[]
    L2=[]
    
    for i in range(w + 2):
        L1.append(".")
    for j in range(h + 2):
            
        L2.append(L1)
        
    L2=np.matrix(L2)    
    
    for i in range(L2.shape[0]):
        for j in range(L2.shape[1]):
            if i == 0 or i == h+1 or j == 0 or j == w+1 :
                L2[i,j] = "T"
            
    return np.array(L2)

def selecionaNo(x,y,G,b,F,a,objetivos):
    
    T = F.copy()
    
    s = 0
    
   
    if G[x+1][y] == '.':
        s += T[x][y][x+1][y]**a * D(x+1,y,objetivos)**b #G[x+1][y]**b D(x+1,y,objetivos)
    
    
    if G[x-1][y] == '.':
        s += T[x][y][x-1][y]**a * D(x-1,y,objetivos)**b #G[x-1][y]**b D(x-1,y,objetivos)
   
    
    if G[x][y+1] == '.':
        s += T[x][y][x][y+1]**a * D(x,y+1,objetivos)**b #G[x][y+1]**b D(x,y+1,objetivos)
    
    
    if G[x][y-1] == '.':
        s += T[x][y][x][y-1]**a * D(x,y-1,objetivos)**b #G[x][y-1]**b D(x,y-1,objetivos)
   
    
    if s == 0: return (-1,-1)
    
    p=np.zeros(4)
    
    if G[x+1][y] == '.':
        p[0] = (T[x][y][x+1][y]**a * D(x+1,y,objetivos)**b) /s #G[x+1][y]**b) / s
    
    
    if G[x-1][y] == '.':
        p[1] = (T[x][y][x-1][y]**a * D(x-1,y,objetivos)**b) /s #G[x-1][y]**b) / s
   
    
    if G[x][y+1] == '.':
        p[2] = (T[x][y][x][y+1]**a * D(x,y+1,objetivos)**b) /s #G[x][y+1]**b) / s
    
    
    if G[x][y-1] == '.':
        p[3] = (T[x][y][x][y-1]**a * D(x,y-1,objetivos)**b) /s #G[x][y-1]**b) / s

    if sum(p) == 0:
        return (-1,-1)

# =============================================================================
#     draw = choice([0,1,2,3], 1, p=p)
#     
#     if draw == 0: return (x+1,y)
#     if draw == 1: return (x-1,y)
#     if draw == 2: return (x,y+1)
#     if draw == 3: return (x,y-1)
# =============================================================================
    
    m=0
    for i in range(len(p)):
        if p[i] > m:
            m = p[i]
    mm=[]
    for i in range(len(p)):
        if p[i]==m:
            mm.append(i)
    draw = choice(mm)
    if draw == 0: return (x+1,y)
    if draw == 1: return (x-1,y)
    if draw == 2: return (x,y+1)
    if draw == 3: return (x,y-1)
   

def ACO(inicio, objetivo, formigas, iteracoes, ins):
    
    #G = grid(n,n)
    h,w=getSize(ins)
    
    T = iniciaFer(h,w)
       
    p = 0.2

    C = 0.6 # Atualização ferormonio
    
    best=[]
        
    a = 0.6
    b = 0.3
    
    for i in range(iteracoes): #iterações
        
        caminhos=[]
        
        for j in range(formigas): #formigas
                
            G = instancia(ins)
        
            busca = objetivo.copy()
        
            x = inicio
            
            path=[x]
            
            # it = 0
            
            br=0
            
            G[x[0]][x[1]] = 'v'
            
            while len(busca) != 0: #and it < n*n: # procura solução
                
                x = selecionaNo(x[0],x[1],G,b,T,a,busca)
            
                if x[0] == -1: 
                    
                    br = 1
                    
                    break                               
                               
                G[x[0]][x[1]] = 'v'

                if x in busca: busca.remove(x)
            
                path.append(x)
                                    
                # it += 1
            
            if br != 1:
                           
                if len(path) < len(best) or len(best) == 0:
                
                    best = path.copy()
            
                caminhos.append(path)
                
        T = (1-p) * T
        
        T = atualizaFerormonio(caminhos,T,C)
        
    return best
# =============================================================================
# 
# h=10
# w=10
# 
# n = 15
# 
# inicio = (1,1)
# objetivo=[]
# while len(objetivo)<10:
#     
#     x = np.random.randint(1,n)
#     
#     y = np.random.randint(1,n)
#     
#     if (x,y) not in objetivo:
#         
#         objetivo.append((x,y))
# 
# formigas = 50
# iteracoes = 200
# 
# tStart = t.time()
# 
# c = ACO(inicio, objetivo, formigas, iteracoes, n)
# 
# tEnd = t.time()
# 
# print("Total Time:", dt.timedelta(seconds = tEnd - tStart))
# 
# plot(c,objetivo,n)
# 
# =============================================================================
