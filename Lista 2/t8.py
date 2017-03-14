# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 16:54:43 2017

@author: wesley150
"""

from q8 import *

lista = Lista1()

lista2 = Lista2()

lista3 = Lista2()

lista2.inserirCabeca(2)
lista2.inserirCabeca(1)

lista3.inserirCabeca(4)
lista3.inserirCabeca(3)


print('Lista2 antes da concatenação')
lista2.imprimirLista()
print('Lista3 antes da concatenação')
lista3.imprimirLista()
print('Lista de retorno:')
lista.concatenat(lista2,lista3).imprimirLista()
print('Lista2 depois da concatenação')
lista2.imprimirLista()
print('Lista3 depois da concatenação')
lista3.imprimirLista()