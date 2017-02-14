# O retangulo tem que ser considerado da seguinte forma:
#       P1                 P2
#
#
#       P3                 P4
#
# Sendo P1...P4 os pontos dos extremos do retangulo.


from retangulo import Retangulo

import imp
q1 = imp.load_source('Ponto', '../q1/ponto.py')

p1 = q1.Ponto();
p2 = q1.Ponto();
p3 = q1.Ponto();
p4 = q1.Ponto();

p1.inserirCoordenadas(0,1);
p2.inserirCoordenadas(1,1);
p3.inserirCoordenadas(0,0);
p4.inserirCoordenadas(1,0);

retangulo = Retangulo(p1,p2,p3,p4);

print ("A area do retângulo eh: %.2f \n" % retangulo.calculaArea())

print (retangulo.verificaQuadrado())


