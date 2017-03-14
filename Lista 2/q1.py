# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 10:36:50 2017

@author: wesley150
"""

class Lista1:
    def __init__(self):
        self.referencia = None
        
    def ordenaCrescente(self, lista):
        if(lista.referencia == None):
            print('Lista vazia, nao tem como ordenar')
            return
        nova_lista = Lista2()
        tempReferencia = lista.referencia
        while(tempReferencia != None):
            nova_lista.inserirCabeca(tempReferencia.valor)
            tempReferencia = tempReferencia.proximo
        tempRef1 = nova_lista.referencia
        tempRef2 = nova_lista.referencia.proximo
        while(tempRef1 != None):
            tempRef2 = tempRef1.proximo
            while(tempRef2 != None):
                if(tempRef1.valor > tempRef2.valor):
                     balde = tempRef1.valor
                     tempRef1.valor = tempRef2.valor
                     tempRef2.valor = balde
                tempRef2 = tempRef2.proximo
            tempRef1 = tempRef1.proximo
        return nova_lista
            
class Lista2:
    def __init__(self):
        self.referencia = None
            
    def inserirCabeca(self,valor):
        novoNo = No(valor)
        tempNo = self.referencia
        self.referencia = novoNo
        self.referencia.proximo = tempNo

        
    def imprimirLista(self):
        tempReferencia = self.referencia        
        while (tempReferencia != None):
            tempNo = tempReferencia
            print (tempNo.valor)
            tempReferencia = tempReferencia.proximo

class No:
    def __init__(self, valor):
        self.proximo = None
        self.valor = valor