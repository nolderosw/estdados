# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 16:40:46 2017

@author: wesley150
"""

class Lista1:
    def __init__(self):
        self.referencia = None
    def concatena(self,lista1,lista2):
        nova_lista = Lista2()
        antigaRef1 = lista1.referencia  
        antigaRef2 = lista2.referencia 
        while(antigaRef1 != None):
            nova_lista.inserirFim(antigaRef1.valor)
            antigaRef1 = antigaRef1.proximo
        while(antigaRef2 != None):
            nova_lista.inserirFim(antigaRef2.valor)
            antigaRef2 = antigaRef2.proximo
        return nova_lista
        
class Lista2:
    def __init__(self):
        self.referencia = None
            
    def inserirCabeca(self,valor):
        novoNo = No(valor)
        tempNo = self.referencia
        self.referencia = novoNo
        self.referencia.proximo = tempNo
    
    def inserirFim(self,valor):
        novoNo = No(valor)
        if(self.referencia == None):
            self.referencia = novoNo
        else:
            tempNo = self.referencia
            while(tempNo.proximo != None):
                tempNo = tempNo.proximo
            tempNo.proximo = novoNo
        
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