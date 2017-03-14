# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 16:50:39 2017

@author: wesley150
"""

class Lista1:
    def __init__(self):
        self.referencia = None
    def concatenat(self,lista1,lista2):
        nova_lista = Lista2()
        Ref1 = lista1.referencia  
        Ref2 = lista2.referencia 
        while(Ref1 != None):
            nova_lista.inserirFim(Ref1.valor)
            nova_lista.inserirFim(Ref2.valor)
            Ref1 = Ref1.proximo
            Ref2 = Ref2.proximo
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