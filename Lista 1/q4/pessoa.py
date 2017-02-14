class Pessoa:

	def __init__(self):
		self.nome = None
		self.ano = None
		self.email = None
	def inserirNome(self,nome):
		self.nome = nome
	def inserirAno(self,ano):
		self.ano = ano
	def inserirEmail(self,email):
		self.email = email
	def obterNome(self):
		return self.nome
	def obterAno(self):
		return self.ano
	def obterEmail(self):
		return self.email
	def obterIdade(self):
		return (2017 - int(self.ano))
