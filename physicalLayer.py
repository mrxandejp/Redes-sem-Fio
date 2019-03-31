#Classe da camada física
import packet as pk
#import node as no
from numpy import linalg as LA
from scipy.spatial import distance

class PhysicalLayer():
    
    def __init__ (self):
        pass

    def send(self, packet, nos_np):
        print("Enviando pacote " +  str(packet.content))
        for i in nos_np:
            if distance.seuclidean(self.pos, i.pos, [1, 1]) == 1:
                print("Enviado do nó " + str(self.pos) + " para o nó " + str(i.pos))
                i.receive(packet)


    def receive(self, packet):
        print("Nó " + str(self.pos) + " recebeu o pacote " + str(packet.content))
        pass
