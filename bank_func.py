import textwrap


def menu():
    menu = textwrap.dedent("""\
    ****** MENU *******
    [D]  \tDepositar
    [S]  \tSacar
    [E]  \tExtrato
    [NC] \tNova Conta
    [LC] \tListar Contas
    [NU] \tNovo usuário
    [X]  \tSair

    >>> Digite a opção desejada: """)

    return input(menu).upper()
    
def retirar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n>>>Saldo insuficiente!<<<\n")
    elif excedeu_limite:
        print("\n>>>Valor acima do limite.\n")
    elif excedeu_saque:
        print("\n>>>Excedeu o limite de saques.\n")
    elif valor > 0:
        saldo -= valor
        extrato += f"\n\tSaque realizado no valor de R$ {valor:.2f}"
        numero_saques +=1
        print("\n\tSaque realizado com sucesso!<<<\n")

    else:
        print("\n>>>Valor inválido.<<<\n")

    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"\n\tDepósito realizado no valor de R$ {valor:.2f}"
        print("\n\tDepósito realizado com sucesso!\n")
    else:
        print("\nValor informado é inválido, tente novamente.\n")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n\t====== EXTRATO =======")
    print("\n Não houve movimentações! \n" if not  extrato else extrato)
    print(f"\n\t Saldo atualizado: R$ {saldo:.2f}")
    print("\t========================")

def main ():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuario = []
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

        elif opcao == "X":
            break




main()


