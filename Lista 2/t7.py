# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 16:41:28 2017

@author: wesley150
"""

from q7 import *

lista = Lista1()

lista2 = Lista2()

lista3 = Lista2()

lista2.inserirCabeca(8)
lista2.inserirCabeca(7)
lista2.inserirCabeca(6)

lista3.inserirCabeca(5)
lista3.inserirCabeca(4)
lista3.inserirCabeca(3)


print('Lista2 antes da concatenação')
lista2.imprimirLista()
print('Lista3 antes da concatenação')
lista3.imprimirLista()
print('Lista de retorno:')
lista.concatena(lista3,lista2).imprimirLista()
print('Lista2 depois da concatenação')
lista2.imprimirLista()
print('Lista3 depois da concatenação')
lista3.imprimirLista()