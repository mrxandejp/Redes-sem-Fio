'''
Trabalho de Redes sem fio
Prof: Fernando Menezes Matos
'''

import node as no
import packet as pk 
import pyshicalLayer as pys


def GenerateNetwork(nodes,range,size): # Função que cria a topologia da rede
	for i in range(nodes):
		n[i] = no.Node(i,random.randint(0,size),random.randint(0,size))

no1 = no.Node(1,2,3)
pkt1 = pk.Packet(10, [0,1,1])
camadaFisica = pys.PyshicalLayer()

camadaFisica.Send(pkt1)