import numpy as np
import random

def cria(n):
    
    # p = random.randrange((n*n)-2*n,n*n)
    p=n*n - 1
    
    q = 100
    
    produtos = []
    
    a=1
    
    for i in range (n*n -1):
    
        if a >= p+1 : a =1    
        
        produtos.append(a)
        
        a+=1
    
    random.shuffle(produtos)
    
    compras = produtos.copy()
    
    produtos.insert(0,-1)
    
    grid = np.zeros((n*n,4))
    grid[:,0] = produtos
    a=b=0
    
    for i in range(0,n*n):
         
        if a >=n: a = 0
        if b >= n: 
            b=0
            a +=1
        
        grid[i][1] = a
        grid[i][2] = b
        grid[i][3] = random.randrange(1,q)
        
        b+=1
        
    grid=grid[grid[:,0].argsort()]
        
    Nome = f'InstanciasCriadas/Grid{n}_P{p}_Q{q}.txt'
    
    s = [n,p,q]
    
    arquivo = open(Nome,'wb')
    np.savetxt(arquivo, s,fmt='%.0f')
    np.savetxt(arquivo, grid,fmt='%.0f')
    arquivo.close()
    
    arquivo = open(f'InstanciasCriadas/Grid{n}_P{p}_Q{q}_Compras.txt','wb')
    
    for i in range(n*5):
    
        r = random.sample(compras,random.randrange(3,15))
        
        r = np.array(r)
    
        np.savetxt(arquivo, r.reshape(1,r.shape[0]),fmt='%.0f')
        
    arquivo.close()
    
n = [5,7,9,10,15,20,25,30,50,75,90,100,150]

for i in n:
    
    cria(i)