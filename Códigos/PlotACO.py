import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def plot(C,G,h,w,ij):
    
    plt.figure(figsize=(10,10))
    
    x, y = np.meshgrid(np.linspace(0,h-1, h), np.linspace(0, w-1, w))

    plt.plot(x, y,'grey') 

    plt.plot(np.transpose(x), np.transpose(y),'grey')
    
    
    x = [i[0] for i in C]
    y = [i[1] for i in C]
    p = [i[2] for i in C]

    plt.plot(x,y,'ko-')
        
    for j in range(len(C)):
        if C[j][2] == 1:
            # plt.annotate(C[j],(x[j],y[j]),color='r')
            plt.plot(x[j],y[j],'go')
        if j == 0:
            # plt.annotate(C[j],(x[j],y[j]),color='r')
            plt.plot(x[j],y[j],'bo')
            
    x=np.array(x)
    y=np.array(y)        
    
    plt.quiver(x[:-1], y[:-1], x[1:]-x[:-1], y[1:]-y[:-1], scale_units='xy', angles='xy', scale=1)
    
    #G = instancia(n)
    
    for i in range(h):
        for j in range(w):
            if G[i][j] == "T":
                plt.plot(i,j,'ro')
                
    plt.axis('off')
    
    plt.savefig(f"../Imagens/G{h}x{w}_{ij+1}.svg",bbox_inches='tight')
    plt.savefig(f"../Imagens/G{h}x{w}_{ij+1}png",bbox_inches='tight',dpi=600)


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

def openResult(i):

    try:

        df = pd.read_csv(f"Resultados/Resultado{i+1}.csv")
    
    except:

        return -1,-1

    instancia = df.columns[0]

    caminho = df.values
    
    return instancia, caminho


#----------------------------------------------------------
for i in range(10):

    instancia, caminho = openResult(i)

    if instancia != -1:

        G, h, w = abreInstancia(instancia)

        print("Plotando Caminho")
        plot(caminho,G,h,w,i)
        print("Imagem salva em: Imagens/test.png")