'''
Trabalho de Redes sem fio
Prof: Fernando Menezes Matos
'''

import node as no
import packet as pk 
import physicalLayer as phy
import random
import numpy as np
from scipy.spatial import distance

def GenerateNetwork(nodes,size, nos): # Função que cria a topologia da rede
    lista = []
    for i in range(nodes):
        while(True):
            rx = random.randint(0, size)
            ry = random.randint(0, size)
            r = [rx, ry]
            if r not in lista: 
                lista.append(r)
                nos.append(no.Node(i,rx,ry))
                break

nos = []

GenerateNetwork(100,9, nos)

nos_np = np.array(nos)
for i in nos_np:
    print(str(i.pos))

pkt1 = pk.Packet(10, [0,1,1])

nos_np[0].send(pkt1, nos_np)
