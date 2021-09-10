# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 19:08:18 2021

@author: Rodrigo
"""

import numpy as np

import random as rd

import time as t

import datetime as dt

def adjacencia(rows, cols):
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
                  
def dist(x1,y1,x2,y2):
    
    r = abs(x1-x2) + abs(y1-y2)
    
    if r > 0: return r
    
    return float("inf")

def ferormonio(Tam):
    
    T = np.zeros((Tam*Tam,Tam*Tam))

    for i in range(Tam*Tam):
        
        for j in range(Tam*Tam):
        
            T[i,j] = 0.1
            
    return T

def atualizaFerormonio(path,C,T):
    
    # for j in range(len(path)):
    
    for i in range(len(path)-1):
            
        T[path[i]][path[i+1]] += C 
            
    return T
    

def selecaoAresta(x, T, a, N, b,Visitados):
    
    p = [0 for i in range(N.shape[0])]
    
    s = 0
    
    # for i in range(N.shape[0]): # vertices não visitados
    for i in naoVisitados: # vertices não visitados
            
        s = s + T[x][i]**a * N[x][i]**b
     
    for y in range(N.shape[0]):
        
        if s == 0:
        
            p[y]=0
        
        else:
        
            t = T[x][y]**a * N[x][y]**b
           
            p[y] = t /  s 
    
    M = []
    
    for i in range(len(p)):
        
        if p[i] == max(p):
            
            M.append(i)
            
    for i in M[:]:
        
        if i in Visitados: M.remove(i)
    
    if len(M) !=0: c = rd.choice(M)
    else: c=-1
       
    return c

def ACO(inicio, objetivo, formigas, iteracoes, Tam):
   
    N = adjacencia(Tam,Tam)

    T = ferormonio(Tam) 
   
    p = 0.5 # redução ferormonio
    
    C = 0.6 # Atualização ferormonio
    
    best=[]
        
    a = 0.6
    b = 0.7
    
    for i in range(iteracoes): #iterações
        
        caminhos=[]
    
        for j in range(formigas): #formigas
                
            naoVisitados=[k for k in range(1,Tam*Tam)]
        
            Visitados=[0]
        
            busca = objetivo.copy()
        
            x = inicio
            
            path=[x]
            
            it = 0
            
            br=0
            
            while len(busca) != 0 and it < Tam*Tam: # procura solução
                
                x = selecaoAresta(x, T, a, N, b, Visitados)
            
                if x == -1: 
                    
                    br = 1
                    
                    break                               
                               
                if x in busca: busca.remove(x)
            
                path.append(x)
                
                Visitados.append(x)
                
                try:
                    
                    naoVisitados.remove(x)
                    
                except:
                    
                    print(x)
                    
                it += 1
            
            if br != 1:
                           
                if len(path) < len(best) or len(best) == 0:
                
                    best = path.copy()
            
                caminhos.append(path)
                            
        T = (1-p) * T
        
        T = atualizaFerormonio(best,C,T)
                
    return best
        
# =============================================================================
# Rodar
# =============================================================================

Tam = 20

inicio = 0

objetivo = [Tam*Tam-1]

formigas = 15

iteracoes = 150
     
naoVisitados=[i for i in range(1,Tam*Tam)]
      
tStart = t.time()

caminho=[]

mediaCaminhos=[]

for i in range(1):

    caminho.append(ACO(inicio, objetivo, formigas, iteracoes, Tam))
    
    mediaCaminhos.append(len(caminho[i]))

tEnd = t.time()

print("Total Time:", dt.timedelta(seconds = tEnd - tStart))

print("Análise")

print("Max:", max(mediaCaminhos))

print("Média:", np.mean(mediaCaminhos))

print("Min:", min(mediaCaminhos))