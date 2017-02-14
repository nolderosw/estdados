import imp
q4 = imp.load_source('Pessoa', '../q4/pessoa.py')

menu = 0
pessoas = []

while (menu != '3'):
	menu = input("Escolha uma das opções abaixo:\n\n1-Cadastrar uma pessoa\n2-Listar pessoas cadastradas\n3-Sair\n\n")
	if(menu == '1'):
		pessoa = q4.Pessoa()
		nome = input("Insira o nome da Pessoa que deseja cadastrar\n")
		pessoa.inserirNome(nome)
		ano = input("Insira o ano de nascimento da Pessoa que deseja cadastrar\n")
		pessoa.inserirAno(ano)
		email = input("Insira o e-mail da Pessoa que deseja cadastrar\n")
		pessoa.inserirEmail(email)
		pessoa = [pessoa.obterNome(),pessoa.obterAno(),pessoa.obterEmail(),pessoa.obterIdade()]
		pessoas.append(pessoa)
	elif(menu == '2'):
		for i in range(len(pessoas)):
			print ("\nPessoa",i+1,":","\n\nNome:",pessoas[i][0],"\nAno de Nascimento:",pessoas[i][1],"\nEmail:",pessoas[i][2],"\nIdade:",pessoas[i][3],"\n")
	elif(menu == '3'):
		for i in range(len(pessoas)):
			print ("\nPessoa",i+1,":","\n\nNome:",pessoas[i][0],"\nAno de Nascimento:",pessoas[i][1],"\nEmail:",pessoas[i][2],"\nIdade:",pessoas[i][3],"\n")
		print ("Obrigado!")
		
