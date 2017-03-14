# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 09:35:14 2017

@author: wesley150
"""

class Lista:
    def __init__(self):
        self.referencia = None
    
    def inserirFim(self,valor):
        novoNo = no(valor)
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
            
    def deslocaUltimoParaPrimeiro(self):
        if(self.referencia == None):
            print('Lista Vazia')
            return
        if(self.referencia.proximo == None):
            print('Lista apenas com um elemento, troca não ocorre')            
            return
        if(self.referencia.proximo.proximo == None):
            inicio = self.referencia
            self.referencia = inicio.proximo
            self.referencia.proximo = inicio
            inicio.proximo = None
            return
        tempRef = self.referencia
        segundo = self.referencia.proximo
        primeiro = self.referencia
        while(tempRef.proximo.proximo != None):
            tempRef = tempRef.proximo
        self.referencia = tempRef.proximo
        self.referencia.proximo = segundo
        primeiro.proximo = None
        tempRef.proximo = primeiro
            
            
                
        
class no:
    def __init__(self,valor):
        self.valor = valor
        self.proximo = None