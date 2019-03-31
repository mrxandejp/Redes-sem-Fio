'''
Trabalho de Redes sem fio
Prof: Fernando Menezes Matos
'''

import node as no
import packet as pk 
import pyshicalLayer as pys
import random
from scipy.spatial import distance_matrix

def GenerateNetwork(nodes,size, n): # Função que cria a topologia da rede
    lista = []
    for i in range(nodes):
        while(True):
            rx = random.randint(0, size)
            ry = random.randint(0, size)
            r = [rx, ry]
            if r not in lista: 
                lista.append(r)
                n.append(no.Node(i,rx,ry))
                break


    #for i in range(nodes):
	#	n[i] = no.Node(i,random.randint(0,size),random.randint(0,size))

n = []
GenerateNetwork(100,10, n)

for i in n:
    print(str(i.pos))



'''
no1 = no.Node(1,2,3)
pkt1 = pk.Packet(10, [0,1,1])
camadaFisica = pys.PyshicalLayer()

camadaFisica.Send(pkt1)
'''