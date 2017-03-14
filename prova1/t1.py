# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 09:39:53 2017

@author: wesley150
"""

from q1 import *

lista = Lista()

lista.inserirFim(1)
lista.inserirFim(2)
lista.inserirFim(3)


print('Lista antes da função')
lista.imprimirLista()

lista.deslocaUltimoParaPrimeiro()
print ('Lista depois da função')
lista.imprimirLista()