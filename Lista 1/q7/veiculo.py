class Veiculo:
	def __init__(self):
		self.nome = None
		self.marca = None
		self.placa = None
	def inserirNome(self,nome):
		self.nome = nome
	def inserirMarca(self,marca):
		self.marca = marca
	def inserirPlaca(self,placa):
		self.placa = placa
	def obterNome(self):
		return self.nome
	def obterMarca(self):
		return self.marca
	def obterPlaca(self):
		return self.placa

	
