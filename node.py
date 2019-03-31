#Classe de nós
from physicalLayer import PhysicalLayer

class Node(PhysicalLayer):
	# Atributos da classe (class atributes)
	# Construtor do objeto (initializer)
	def __init__(self, id, posX, posY):
		self.id = id
		self.pos = [posX,posY]
