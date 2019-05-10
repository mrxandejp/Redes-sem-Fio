'''
Trabalho de Redes sem fio
Prof: Fernando Menezes Matos
'''

import node as no
import packet as pk 
import physicalLayer as phy
import random
import numpy as np
import logging as log
from scipy.spatial import distance

log.basicConfig(filename='redes.log',filemode='w',level=log.DEBUG)

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

GenerateNetwork(4,1, nos)

nos_np = np.array(nos)
for i in nos_np:
    log.info(str(i.pos))

pkt1 = pk.Packet(0, [0,0,0])
pkt1.link_header([0,1])
pkt2 = pk.Packet(1, [0,0,1])
pkt2.link_header([2,1])
pkt3 = pk.Packet(2, [0,1,0])
pkt3.link_header([0,1])

pkt =  [pkt1, pkt2, pkt3]

qt_pkts = len(pkt)
print(qt_pkts)
pkt_enviado = []

while(True):
    if len(pkt) != 0:
        for i in nos_np:
            i.busy_tone = 0
            pass
        count = 0
        for i in pkt:
            if nos_np[i.mac_header[0][0]].busy_tone == 0:
                no = nos_np[i.mac_header[0][0]].id 
                #print("Nó = " + str(no) + " ----> Enviando pacote " + str(i.content))
                enviou = nos_np[i.mac_header[0][0]].link_send(nos_np, i)
                if enviou:
                    pkt_enviado.append(count)
                    count+=1    
            else:
                print("BUSY TONE: " + str(nos_np[i.mac_header[0][0]].busy_tone))

        print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
        print(str(pkt_enviado))
        for i in pkt_enviado:
            #print("VIZINHOS: " + str(nos_np[pkt[i].mac_header[0][0]].vizinhos))
            if len(nos_np[pkt[i].mac_header[0][0]].vizinhos):
                for j in nos_np[pkt[i].mac_header[0][0]].vizinhos:
                    no_recieve = j
                    nos_np[no_recieve].recieve(pkt[i], no_recieve,nos_np)
    
            nos_np[pkt[i].mac_header[0][0]].busy_tone = 0
            pkt.pop(i)   
        pkt_enviado.clear()
    else:
        print("ENVIADO TODOS OS PACOTES")
        break
    pass

#nos_np[0].send(pkt1, nos_np)
#nos_np[0].send_rts(1, 2, 1, 0,nos_np)
