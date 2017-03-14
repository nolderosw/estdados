# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 16:09:38 2017

@author: wesley150
"""

from q6 import *

lista = Lista1()

lista2 = Lista2()

lista2.inserirCabeca(13)
lista2.inserirCabeca(11)
lista2.inserirCabeca(8)
lista2.inserirCabeca(7)
lista2.inserirCabeca(6)
lista2.inserirCabeca(5)
lista2.inserirCabeca(4)
lista2.inserirCabeca(3)
lista2.inserirCabeca(2)

print('Lista2 antes da função')
lista2.imprimirLista()
print('Lista de retorno:')
lista.NPISP(lista2)
print('Lista2 depois da função')
lista2.imprimirLista()