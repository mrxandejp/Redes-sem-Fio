#Classe da camada de enlace
from physicalLayer import PhysicalLayer
import packet as pk 
from packet import Packet
from scipy.spatial import distance

class LinkLayer(PhysicalLayer):

    def __init__ (self):
        pass

    def link_send(self, nos_np, pkt):
        ocupado = 0
        self.busy_tone = 1
        self.vizinhos.clear()
        for i in nos_np:
            if distance.seuclidean(self.pos, i.pos, [1, 1]) == 1:
                #print("Enviado do nó " + str(self.pos) + " para o nó " + str(i.pos))
                if i.busy_tone == 1:
                    ocupado = 1
                    self.vizinhos.clear()
                    break
                else:
                    i.busy_tone = 1
                    self.vizinhos.append(i.id)
        if ocupado:
            print("CANAL OCUPADO")
            return 0
        else:        
            for i in self.vizinhos:
                super().send(pkt, nos_np, i)
        #nos_np[no].vizinhos = super().send(pkt, nos_np)
        print("VIZINHOS " + str(self.vizinhos))
        return 1

    def link_recieve(self, nos_np, pkt, no_recieve):
        nos_np[no_recieve].busy_tone = 0
        if nos_np[no_recieve].id == pkt.mac_header[0][1]:
            print("RECEBEU O PACOTE -- enlace -- Nó = " + str(nos_np[no_recieve].id))
            pass
        else:
            print("NÃO É PARA MIM -- enlace -- Nó = " + str(nos_np[no_recieve].id))

    '''
		FRAME CONTROL
		0 ----> DADO
		1 ----> RTS
		2 ----> CTS
		3 ----> ACK
	
    def send_rts(self, frame_control, duration, recieve_address, transmit_address, nos_np):
        pkt_rts = pk.Packet(2,-1)
        pkt_rts.link_header([frame_control,duration,recieve_address, transmit_address])
        super().send(pkt_rts, nos_np)

    def send_cts(self, frame_control, duration, recieve_address, nos_np):
        pkt_cts = pk.Packet(3,-1)
        pkt_cts.link_header([frame_control,duration,recieve_address])
        print("PACOTE CTS")
        print(pkt_cts.mac_header)
        super().send(pkt_cts, nos_np)
        pass

    def link_recieve(self, pkt_recieve, no_recieve, nos_np):
        print(pkt_recieve.mac_header)
        if pkt_recieve.mac_header[0][0] == 0:
            #DADO
            pass
        elif pkt_recieve.mac_header[0][0] == 1:
            print("RECEBEU RTS!!")
            if(pkt_recieve.mac_header[0][2] == no_recieve.id):
                print("enviando cts")
                self.send_cts(2, 2, pkt_recieve.mac_header[0][3], nos_np)
            else:
                print("NÃO SOU EU")
            pass
        elif pkt_recieve.mac_header[0][0] == 2:
            print("RECEBEU CTS!!")
            pass
        elif pkt_recieve.mac_header[0][0] == 3:
            #ack
            pass
    '''