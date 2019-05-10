#Classe de nós
from linkLayer import LinkLayer

class Node(LinkLayer):
	# Atributos da classe (class atributes)
	# Construtor do objeto (initializer)
	
	def __init__(self, id, posX, posY):
		self.id = id
		self.pos = [posX,posY]
		self.busy_tone = 0
		self.vizinhos = []
