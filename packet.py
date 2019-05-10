# Classe de pacotes

class Packet(object): 
	# Atributos da classe (class atributes)
	# Construtor do objeto (initializer)
	

	#def __new__(cls, *args, **kwargs):
	#	obj = super(Packet,cls).__new__(cls)
	#    obj._from_base_class = type(obj) == Packet
    #    return obj

	def __init__(self, id, content ):
		self.id = id
		self.content = content # Conteúdo do pacote (lista)
		self.mac_header = []
	
	def link_header(self,dado):
		self.mac_header.append(dado)
		