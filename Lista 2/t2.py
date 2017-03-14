# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 14:45:14 2017

@author: wesley150
"""

from q2 import *

lista = Lista1()

lista2 = Lista2()

lista2.inserirCabeca(5)
lista2.inserirCabeca(4)
lista2.inserirCabeca(3)
lista2.inserirCabeca(2)
print('Lista2 antes da função')
lista2.imprimirLista()
print('Lista de retorno:')
lista.parZero(lista2).imprimirLista()
print('Lista2 depois da função')
lista2.imprimirLista()