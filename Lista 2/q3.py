# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 15:01:15 2017

@author: wesley150
"""

class Lista1:
    def __init__(self):
        self.referencia = None
    def parZero(self,lista, parametro):
        if(lista.referencia == None):
            print('Lista vazia')
            return 
        nova_lista = Lista2()
        if(parametro > lista.tamanho()):
            print('Parametro Maior que a lista')
            return nova_lista      
        antigaRef = lista.referencia        
        cont = 0
        while(antigaRef != None):
            if(cont >= parametro-1):
                nova_lista.inserirFim(antigaRef.valor)
            antigaRef = antigaRef.proximo
            cont += 1
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
        
    def tamanho(self):
        tamanho = 1
        tempReferencia = self.referencia
        while (tempReferencia.proximo != None):
            tamanho += 1
            tempReferencia = tempReferencia.proximo
        return tamanho

class No:
    def __init__(self, valor):
        self.proximo = None
        self.valor = valor