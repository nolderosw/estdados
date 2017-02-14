import imp
q4 = imp.load_source('Pessoa', '../q4/pessoa.py')

pessoa1 = q4.Pessoa();
pessoa2 = q4.Pessoa();
pessoa3 = q4.Pessoa();

pessoa1.inserirNome('Maria')
pessoa2.inserirNome('Joao')
pessoa3.inserirNome('Pedro')

pessoa1.inserirAno(1990)
pessoa2.inserirAno(1982)
pessoa3.inserirAno(1964)

pessoa1.inserirEmail('maria@gmail.com')
pessoa2.inserirEmail('joao@gmail.com')
pessoa3.inserirEmail('pedro@gmail.com')

print ("Pessoa1:","\n\nNome:",pessoa1.obterNome(),"\nAno de Nascimento:",pessoa1.obterAno(),"\nEmail:", pessoa1.obterEmail(),"\nIdade:",pessoa1.obterIdade(),"\n")
print ("Pessoa2:","\n\nNome:",pessoa2.obterNome(),"\nAno de Nascimento:",pessoa2.obterAno(),"\nEmail:", pessoa2.obterEmail(),"\nIdade:",pessoa2.obterIdade(),"\n")
print ("Pessoa3:","\n\nNome:",pessoa3.obterNome(),"\nAno de Nascimento:",pessoa3.obterAno(),"\nEmail:", pessoa3.obterEmail(),"\nIdade:",pessoa3.obterIdade(),"\n")
