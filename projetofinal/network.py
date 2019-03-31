'''
Trabalho de Redes sem fio
Prof: Fernando Menezes Matos
'''
import random

# Declaração das classes:
class Packet: 
	# Atributos da classe (class atributes)
	# Construtor do objeto (initializer)
	def _init_(self, id):
		self.id = id
		self.content = [] # Conteúdo do pacote (lista)

class Node:
	# Atributos da classe (class atributes)
	pass
	# Construtor do objeto (initializer)
	def _init_(self, id, posX, posY):
		self.id = id
		self.pos = [posX,posY]

'''
class Router(Node):
	# Atributos da classe (class atributes)
	pass
	# Construtor do objeto (initializer)
	def _init_(self):
		self.id = id



class Host(Node):
	# Atributos da classe (class atributes)
	pass
	# Construtor do objeto (initializer)
	def _init_(self):
		self.id = id

	# Método da instância
'''

def GenerateNetwork(nodes,range,size) # Função que cria a topologia da rede
	for i in range(nodes):
		n[i] = Node(i,random.randint(0,size),random.randint(0,size))



class PyshicalLayer(Node):

	def Send(self,packet):
		self.pos
		p = packet.id

