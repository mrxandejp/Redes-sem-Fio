#Classe da camada de redes
from linkLayer import LinkLayer
import packet as pk 
from packet import Packet
from scipy.spatial import distance

class NetworkLayer(LinkLayer):
    def __init__ (self):
        pass

    def route_request(self, id_flood, origem, destino, nos_np):
        pkt_flood = pk.Packet(id_flood,[-1],origem, destino)
        pkt_flood.set_flooding()
        super().enlace(nos_np, pkt_flood)
        pass        
    
    def route_response(self):
        pass

    def net_recieve(self, pkt_recieve, nos_np, no_recieve):
        print("-------NET RECIEVE-------")
        if pkt_recieve.flooding == 1:
            if pkt_recieve.header[1] == nos_np[no_recieve].id:
                tam_net_header = len(pkt_recieve.net_header)
                next_address = pkt_recieve.net_header[tam_net_header-1]
                for key in pkt_recieve.net_header:
                    nos_np[no_recieve].rotas[key] = next_address
                    pass
                self.route_response()
                pass
            else:
                tam_net_header = len(pkt_recieve.net_header)
                next_address = pkt_recieve.net_header[tam_net_header-1]
                for key in pkt_recieve.net_header:
                    nos_np[no_recieve].rotas[key] = next_address
                    pass
                pkt_recieve.network_header(nos_np[no_recieve].id)
                print("NETWORK HEADER ---> " + str(pkt_recieve.net_header))
                pkt_recieve.mac_header.clear()
                super().enlace(nos_np, pkt_recieve)
                pass
            pass
        else:
            pass
        pass