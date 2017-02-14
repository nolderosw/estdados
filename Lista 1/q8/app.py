import imp
q7 = imp.load_source('Veiculo', '../q7/veiculo.py')

menu = 0
veiculos = {}

while (menu != '3'):
	menu = input("Escolha uma das opções abaixo:\n\n1-Cadastrar um veículo\n2-Listar veículos cadastrados\n3-Sair\n\n")
	if(menu == '1'):
		veiculo = q7.Veiculo()
		nome = input("Insira o nome do veículo que deseja cadastrar\n")
		veiculo.inserirNome(nome)
		marca = input("Insira a marca do veículo que deseja cadastrar\n")
		veiculo.inserirMarca(marca)
		placa = input("Insira a placa do veículo que deseja cadastrar\n")
		if(placa in veiculos):
			print ("\nErro: Veículo ja cadastrado, tente novamente!!!\n")
		else:
			veiculo.inserirPlaca(placa)
			veiculos[veiculo.obterPlaca()] = [veiculo.obterNome(),veiculo.obterMarca()]
	elif(menu == '2'):
		for i in veiculos:
			print("\nPlaca:",i,"\nNome:",veiculos[i][0],"\nMarca:",veiculos[i][1],"\n")
			
	elif(menu == '3'):
		print ("\nObrigado!")
