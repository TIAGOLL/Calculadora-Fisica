import os
from queue import Queue
import sys
from abc import ABC, abstractmethod

class infoContas(ABC):
	@abstractmethod
	def infomarTipoConta(self):
		pass

class contaFisica():
    def __init__(self, forcaPeso = None, gravidade = None, aceleracao = None, fila = Queue()):
        self._forcaPeso = forcaPeso
        self._gravidade = gravidade
        self._aceleracao = aceleracao
        self._fila = fila

    def iniciar(self):
        print("\n" * 100)
        print("Digite [1] para escolher um exercício com atrito")
        print("Digite [2] para escolher um exercício sem atrito")
        print("Digite [3] para ver seu histórico")
        print("Digite [-1] para encerrar o programa")

        escolhaUsuario = int(input("Informe: "))
        print(escolhaUsuario)
        return escolhaUsuario    
    
    def mostrarOpcoes(self, escolha):
        if escolha != 1 and escolha != 2 and escolha != 3 and escolha != -1:
            print("\n" * 100)
            print("Por favor, insira uma opção válida")
            os.system('pause')
            return

        elif escolha == -1:
            print("\n" * 100)
            print("Programa encerrado!")
            sys.exit()
            
        while True:
            if escolha == 1:
                print("\n" * 130)
                print("Selecione 1 caso esteja faltando a FORÇA PESO")
                print("Selecione 2 caso esteja faltando a MASSA DO OBJETO")
                print("Selecione 3 caso esteja faltando a GRAVIDADE")
                print("Selecione 4 caso esteja faltando a ACELERAÇÃO")
                print("Selecione 5 caso esteja faltando a FORÇA DE ATRITO")
                opcao = int(input())
                if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5:
                    print("\n" * 100)
                    print("Por favor, insira uma opção válida")
                    os.system('pause')
                    return
                return opcao

            elif escolha == 2:
                print("\n" * 130)
                print("Selecione 1 caso esteja faltando a FORÇA PESO")
                print("Selecione 2 caso esteja faltando a MASSA DO OBJETO")
                print("Selecione 3 caso esteja faltando a GRAVIDADE")
                print("Selecione 4 caso esteja faltando a ACELERAÇÃO")
                opcao = int(input())
                if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
                    print("\n" * 100)
                    print("Por favor, insira uma opção válida")
                    os.system('pause')
                    return
                return opcao


            elif escolha == 3:
                print("\n" * 100)
                if len(self._fila.queue) == 0:
                    print("\n" * 100)
                    print('Seu histórico está vazio!')
                    os.system('pause')
                else:
                    print("\n" * 100)
                    print('Seu histórico é: ')
                    for i in range(len(self._fila.queue)):
                        print(f'Resultado {i+1} >>> ' + str(self._fila.queue[i]))
                    os.system('pause')
                return

    def criarArquivoHistorico(self):
        aux = 1
        arquivoHistorico = open('Historico de Resultados', 'w')
        for resultado in self._fila.queue:
            arquivoHistorico.write(f'Resultado {aux} >>> ' + str(resultado) + '\n')
            aux += 1
        arquivoHistorico.close()

    @property
    def forcaPeso(self):
        return self._forcaPeso
    
    @forcaPeso.setter
    def forcaPeso(self, forcaPeso):
        self._forcaPeso = forcaPeso

    @property
    def gravidade(self):
        return self._gravidade
    
    @gravidade.setter
    def gravidade(self, gravidade):
        self._gravidade = gravidade
    
    @property
    def aceleracao(self):
        return self._aceleracao
    
    @aceleracao.setter
    def aceleracao(self, aceleracao):
        self._aceleracao = aceleracao
    

    