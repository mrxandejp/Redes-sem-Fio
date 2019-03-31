#Classe da camada física
import packet as pk

class PyshicalLayer():

    def Send(self, packet):
        p = packet.content
        print("Enviando pacote " +  str(p))

