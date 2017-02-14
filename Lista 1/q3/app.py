# O retangulo1 tem que ser considerado da seguinte forma:
#       P1                 P2
#
#
#       P3                 P4
#
# Sendo P1...P4 os pontos dos extremos do retangulo.


# O retangulo2 tem que ser considerado da seguinte forma:
#       P5                 P6
#
#
#       P7                 P8
#
# Sendo P5...P8 os pontos dos extremos do retangulo.



import imp
q2 = imp.load_source('Retangulo', '../q2/retangulo.py')

import imp
q1 = imp.load_source('Ponto', '../q1/ponto.py')

p1 = q1.Ponto();
p2 = q1.Ponto();
p3 = q1.Ponto();
p4 = q1.Ponto();
p5 = q1.Ponto();
p6 = q1.Ponto();
p7 = q1.Ponto();
p8 = q1.Ponto();

p1.inserirCoordenadas(0,1);
p2.inserirCoordenadas(1,1);
p3.inserirCoordenadas(0,0);
p4.inserirCoordenadas(1,0);
p5.inserirCoordenadas(0,2);
p6.inserirCoordenadas(1,2);
p7.inserirCoordenadas(0,0);
p8.inserirCoordenadas(1,0);

retangulo1 = q2.Retangulo(p1,p2,p3,p4);
retangulo2 = q2.Retangulo(p5,p6,p7,p8);

print ("A area do retângulo 1 eh: %.2f \n" % retangulo1.calculaArea())

print (retangulo1.verificaQuadrado())

print ("\nA area do retângulo 2 eh: %.2f \n" % retangulo2.calculaArea())

print (retangulo2.verificaQuadrado())
