# O retangulo tem que ser considerado da seguinte forma:
#       P1                 P2
#
#
#       P3                 P4
#
# Sendo P1...P4 os pontos dos extremos do retangulo.


import imp
q1 = imp.load_source('Ponto', '../q1/ponto.py')

import math

class Retangulo:
	
	def __init__(self,p1,p2,p3,p4):
		self.p1 = p1
		self.p2 = p2
		self.p3 = p3
		self.p4 = p4
	def calculaArea(self):
		distp1p3 = math.sqrt(((float(self.p1.exibirCoordenadas()[0])-float(self.p3.exibirCoordenadas()[0]))**2) + (float(self.p1.exibirCoordenadas()[1])-float(self.p3.exibirCoordenadas()[1]))**2)
		distp3p4 = math.sqrt(((float(self.p3.exibirCoordenadas()[0])-float(self.p4.exibirCoordenadas()[0]))**2) + (float(self.p3.exibirCoordenadas()[1])-float(self.p4.exibirCoordenadas()[1]))**2)
		area = distp1p3*distp3p4
		
		return area
	def verificaQuadrado(self):
		if((math.sqrt(((float(self.p1.exibirCoordenadas()[0])-float(self.p3.exibirCoordenadas()[0]))**2) + (float(self.p1.exibirCoordenadas()[1])-float(self.p3.exibirCoordenadas()[1]))**2)) == (math.sqrt(((float(self.p3.exibirCoordenadas()[0])-float(self.p4.exibirCoordenadas()[0]))**2) + (float(self.p3.exibirCoordenadas()[1])-float(self.p4.exibirCoordenadas()[1]))**2))):
			return "Eh um quadrado"
		else:
			return "Nao eh um quadrado"
		
		
