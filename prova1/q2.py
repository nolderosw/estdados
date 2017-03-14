# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:19:23 2017

@author: wesley150
"""

class Pilha:
    def __init__(self):
        self.referencia = None

    def push(self, dado):
        novoNo = No(dado)
        novoNo.proximo = self.referencia
        self.referencia = novoNo

    def pop(self):
        resultado = None
        if(self.referencia is not None):
            tempNo = self.referencia
            self.referencia = tempNo.proximo
            tempNo.proximo = None
            resultado = tempNo.dado
        return resultado

    def isEmpty(self):
        if(self.referencia is None):
            return True
        else:
            return False

    def __str__(self):
        return "teste"
        
    def tamanho(self):
        aux = Pilha()        
        tamanho = 0
        while(self.referencia != None):
            tamanho += 1
            aux.push(self.pop())
        while(aux.referencia != None):
            self.push(aux.pop())
        return tamanho
    
    def desempilharElementoDoMeio(self):
        aux = Pilha()        
        cont = 0        
        while(cont < int(self.tamanho()/2)):
            aux.push(self.pop())
            cont += 1
        meio = self.pop()
        while(aux.referencia != None):
            self.push(aux.pop())
        return meio
class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None