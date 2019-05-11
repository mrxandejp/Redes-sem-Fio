#Classe da camada física
import packet as pk
#import node as no
from numpy import linalg as LA
from scipy.spatial import distance
import logging as log

class PhysicalLayer():
    
    def __init__ (self):
        pass

    def send(self, packet, nos_send):
        log.info("Enviando pacote " +  str(packet.content))
        #print("Enviando pacote " +  str(packet.content))
        print("Enviado do nó " + str(self.id) + " para o nó " + str(nos_send.id))
        
        
        
        '''
        vizinhos = []
        for i in nos_np:
            if distance.seuclidean(self.pos, i.pos, [1, 1]) == 1:
                #print("Enviado do nó " + str(self.pos) + " para o nó " + str(i.pos))
                i.busy_tone = 1
                self.busy_tone = 1
                log.info("Enviado do nó " + str(self.id) + " para o nó " + str(i.id))
                print("Enviado do nó " + str(self.id) + " para o nó " + str(i.id))
                #i.receive(packet, i, nos_np)
                vizinhos.append(i.id)
        return vizinhos
        '''

    def recieve(self, packet, no_recieve, nos_np):
        #print("Nó " + str(self.pos) + " recebeu o pacote " + str(packet.content))
        #no_recieve.link_recieve(packet, no_recieve, nos_np)
        nos_np[no_recieve].link_recieve(nos_np, packet, no_recieve)
        log.info("Nó " + str(self.id) + " recebeu o pacote " + str(packet.content))
        pass
