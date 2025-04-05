from bank_func import *


def main ():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []


    while True:
        opcao = menu()

        if opcao == "D":
            valor = float(input("Informe o valor do depósito: R$ "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "S":
            valor = float(input("Informe o valor do saque: R$ "))

            saldo, extrato, numero_saques = retirar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "E":
            exibir_extrato(saldo, extrato=extrato)

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




















































