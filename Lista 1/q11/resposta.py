a = 10
#nesse momento, é alocado um espaço na memória para o inteiro a
b = a
#nesse momento, b recebe um apontador para a
b = 30
#nesse momento, o inteiro b recebe um novo endereço na memoria e o anterior é perdido
a = b
#nesse momento, a recebe um apontador para b
a = 20
#nesse momento, o inteiro a recebe um novo endereço na memoria e o anterior é perdido
