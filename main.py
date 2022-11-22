from contaFisica import *
from comAtrito import *
from semAtrito import *

def escolhaUsuario(opcaoConta):
    if opcaoConta == 1 and escolha == 1:
        contaComAtrito.calcularPeso()
        contaComAtrito.infomarTipoConta()
    elif opcaoConta == 2 and escolha == 1:
        contaComAtrito.calcularMassa()
        contaComAtrito.infomarTipoConta()
    elif opcaoConta == 3 and escolha == 1:
        contaComAtrito.calcularGravidade()
        contaComAtrito.infomarTipoConta()
    elif opcaoConta == 4 and escolha == 1:
        contaComAtrito.calcularAceleracao()
        contaComAtrito.infomarTipoConta()
    elif opcaoConta == 5 and escolha == 1:
        contaComAtrito.calcularForcatrito()
        contaComAtrito.infomarTipoConta()

    elif opcaoConta == 1 and escolha == 2:
        contaSemAtrito.calcularPeso()
        contaSemAtrito.infomarTipoConta()
    elif opcaoConta == 2 and escolha == 2:
        contaSemAtrito.calcularMassa()
        contaSemAtrito.infomarTipoConta()
    elif opcaoConta == 3 and escolha == 2:
        contaSemAtrito.calcularGravidade()
        contaSemAtrito.infomarTipoConta()
    elif opcaoConta == 4 and escolha == 2:
        contaSemAtrito.calcularAceleracao()
        contaSemAtrito.infomarTipoConta()
    else:
        print('Digite uma opção válida!')


while True:
    print("\n" * 100)
    inicio = contaFisica()
    contaComAtrito = comAtrito()
    contaSemAtrito = semAtrito()
    escolha = inicio.iniciar()
    opcaoConta = inicio.mostrarOpcoes(escolha)
    escolhaUsuario(opcaoConta)
    
    inicio.criarArquivoHistorico()

