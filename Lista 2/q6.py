# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 16:07:34 2017

@author: wesley150
"""

class Lista1:
    def __init__(self):
        self.referencia = None
    def NPISP(self,lista):
        if(lista.referencia == None):
            print('Lista vazia')
            return 
        tempReferencia = lista.referencia
        quantidade = 0        
        pares = 0
        impares = 0
        soma = 0
        primos = 0
        while(tempReferencia != None):
            if(tempReferencia.valor%2 == 0):
                pares += 1
                soma += tempReferencia.valor
                quantidade += 1
            else:
                impares += 1
                soma += tempReferencia.valor
                quantidade += 1
                if(tempReferencia.valor == 2 or tempReferencia.valor == 3 or tempReferencia.valor == 5 or tempReferencia.valor == 7):
                    primos += 1
                elif(tempReferencia.valor%3 != 0 and tempReferencia.valor%5 != 0 and tempReferencia.valor%7 != 0):
                    primos += 1
            tempReferencia = tempReferencia.proximo
        print('Quantidade de numeros:',quantidade)
        print('Quantidade de numeros pares:',pares)
        print('Quantidade de numeros impares:',impares)
        print('Quantidade de numeros primos:',primos)
        print('Soma dos numeros:',soma)
        return 
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