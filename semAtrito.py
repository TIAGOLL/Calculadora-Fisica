from contaFisica import *
import os
import math

class semAtrito(contaFisica, infoContas):
    def __init__(self, forcaPeso = None, gravidade = None, aceleracao = None):
        super().__init__(forcaPeso, gravidade, aceleracao)
    
    def infomarTipoConta(self):
        print("\n" * 130)
        print('Você realizou uma conta que não possuía atrito!')
        os.system('pause')

    def calcularPeso(self):
        m = int(input("Informe a massa: "))
        g = float(input("Informe a força da gravidade: "))
        ang = int(input("Informe a angulação do plano: "))
        p = round(m * g * math.cos(math.radians(ang)), 2)
        print("\n" * 130)
        print("A força peso é igual a: ", p)
        self._fila.put(p)
        os.system('pause')
 
    def calcularGravidade(self):
        p = int(input("Informe a força peso (EM NEWTONS): "))
        m = float(input("Informe a massa: "))
        ang = int(input("Informe a angulação do plano: "))
        g = round(p/(m * math.cos(math.radians(ang))), 2)
        self._fila.put(g)
        print("\n" * 130)
        print("A gravidade do local é de: ", g)
        os.system("pause")

 
    def calcularAceleracao(self):
        g = float(input("Informe a força da gravidade: "))
        ang = int(input("Informe a angulação do plano: "))
        coe = float(input("Informe o coeficiente de atrito: "))
        a = round(g * (math.sin(math.radians(ang)) - coe * math.cos(math.radians(ang))), 2)
        self._fila.put(a)
        print("\n" * 130)
        print("A aceleração de queda do objeto no plano é de: ", a)
        os.system("pause")


    def calcularMassa(self):
        p = int(input("Informe a força peso (EM NEWTONS): "))
        g = float(input("Informe a força da gravidade: "))
        ang = int(input("Informe a angulação do plano: "))
        m = round(p/(g * math.cos(math.radians(ang))), 2)
        self._fila.put(m)
        print("\n" * 130)
        print("A massa do objeto é igual a: ",m)
        os.system("pause")
 
 
    @property
    def escolha(self):
        return self._escolha
 
    @escolha.setter
    def escolha(self, escolha):
        self._escolha = escolha

