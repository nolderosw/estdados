# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 15:25:41 2017

@author: wesley150
"""

from q4 import *

lista = Lista1()

lista2 = Lista2()

lista2.inserirCabeca(8)
lista2.inserirCabeca(8)
lista2.inserirCabeca(5)
lista2.inserirCabeca(5)
lista2.inserirCabeca(2)
lista2.inserirCabeca(2)
lista2.inserirCabeca(1)

print('Lista2 antes da função')
lista2.imprimirLista()
print('Lista de retorno:')
lista.removeDup(lista2).imprimirLista()
print('Lista2 depois da função')
lista2.imprimirLista()