# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 19:28:14 2021

@author: Rodrigo
"""

from ACO3 import *

import numpy as np
import time as t
import datetime as dt

ins = "../Instâncias/M_30x30.txt"

_G = instancia(ins)

_h,_w = getSize(ins)

_N = 5

_x = np.random.randint(1,_w-1)
    
_y = np.random.randint(1,_h-1)

while True :
    
    if  _G[_x][_y] != "T":
    
        break
    
    _x = np.random.randint(1,_w-1)
        
    _y = np.random.randint(1,_h-1)

inicio = (_x,_y)

# inicio = (1,1)

objetivo = []

while len(objetivo)<1:
    
    _x = np.random.randint(1,_w)
    
    _y = np.random.randint(1,_h)
    
    if (_x,_y) not in objetivo and (_x,_y) != inicio and _G[_x][_y] != "T" :
        
        objetivo.append((_x,_y))

formigas = 15

iteracoes = 100

caminhos = []

tc = []

tStart = t.time()

for i in range(_N):
    
    c = ACO(inicio, objetivo, formigas, iteracoes, ins)
    
    if len(c) > 0:
    
        caminhos.append(c)

        tc.append(len(c))

tEnd = t.time()

print("Total Time:", dt.timedelta(seconds = tEnd - tStart))

for i in range(len(caminhos)):

    plot(caminhos[i],objetivo, ins)
