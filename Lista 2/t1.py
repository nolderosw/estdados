# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 10:47:04 2017

@author: wesley150
"""

from q1 import *

lista = Lista1()

lista2 = Lista2()

lista2.inserirCabeca(2)
lista2.inserirCabeca(3)
lista2.inserirCabeca(4)
lista2.inserirCabeca(5)

print('Lista2 antes da ordenação:')
lista2.imprimirLista()
print ('\nLista de retorno:')
lista.ordenaCrescente(lista2).imprimirLista()
print('Lista2 depois da ordenação:')
lista2.imprimirLista()
