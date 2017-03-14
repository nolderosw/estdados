# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 11:03:30 2017

@author: wesley150
"""
class Fila:
    def __init__(self):
        self.refInicial = None
        self.refFinal = None

    def inserirFimFila(self, dado):
        novoNo = No(dado)

        if(self.refInicial is None):
            self.refInicial = novoNo
            self.refFinal = novoNo
        else:
            self.refFinal.proximo = novoNo
            self.refFinal = novoNo
            
    def removerInicioFila(self):
        resultado = None

        if(self.refInicial is None):
            return resultado

        tempNo = self.refInicial
        resultado = tempNo.dado

        if(self.refInicial is self.refFinal):
            self.refInicial = None
            self.refFinal = None
        else:
            self.refInicial = tempNo.proximo
            tempNo.proximo = None

        return resultado
        
    def obterSomaValores(self):
        aux = Fila()
        somatorio = 0
        while(self.refInicial != None and self.refFinal != None):
            temp = self.removerInicioFila()            
            somatorio += temp 
            aux.inserirFimFila(temp)
        while(aux.refInicial != None and aux.refFinal != None):          
            self.inserirFimFila(aux.removerInicioFila())
        return somatorio

class No:
    def __init__(self, valor):
        self.dado = valor
        self.proximo = None