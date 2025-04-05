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

def criar_usuario(usuarios):
    cpf = input("Informe o CPF, 'somente números': ")

    # Verificar se há user cadastrado no CPF informado
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("\tJá existe usuário com o CPF informado!")
            return
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço(rua, número, bairro, cidade/Estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereço": endereco
    })
    print("\n>>> Usuário cadastrado com sucesso! <<<\n")


    print("\nUsuário cadastrado com sucesso!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")

    # Verificar se o user está cadastrado
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("\n\t=== Conta cadastrada com sucesso! ===")
            return {
                "agencia": agencia,
                "numero_conta": numero_conta,
                "usuario": usuario
            }
    print("\n\t=== Usuário não cadastrado===")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print(textwrap.dedent(linha))

