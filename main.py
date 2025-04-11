from bank_class import *


def main ():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    limite = 500
    usuarios = []
    contas = []


    while True:
        opcao = menu()

        if opcao == "D":
            depositar(contas)

        elif opcao == "S":
            retirar(contas)

        elif opcao == "E":
            exibir_extrato(contas)

        elif opcao == "NU":
            criar_usuario(usuarios)

        elif opcao == "NC":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "LC":
            listar_contas(contas)



        elif opcao == "X":
            break




main()




















































