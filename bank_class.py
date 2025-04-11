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

def localizar_conta_por_cpf(cpf, contas):
    for conta in contas:
        if conta["usuario"]["cpf"] == cpf:
            return conta
    return None

def depositar(contas):
    cpf = input("Informe o CPF do titular: ")
    conta = localizar_conta_por_cpf(cpf, contas)

    if conta:
        valor = float(input("Informe o valor a depositar: R$ "))
        if valor > 0:
            conta["saldo"] += valor
            conta["extrato"] += f"\nDepósito: R$ {valor:.2f}"
            print("\n>>> Depósito realizado com sucesso! <<<")
        else:
            print("\n>>> Valor inválido para depósito. <<<")
    else:
        print("\n>>> Conta não localizada. <<<")


def retirar(contas, limite=500, limite_saques=3):
    cpf = input("Informe o CPF do titular: ")
    conta = localizar_conta_por_cpf(cpf, contas)

    if not conta:
        print("\n>>> Conta não encontrada. <<<")
        return

    valor = float(input("Informe o valor do saque: R$ "))
    excedeu_saldo = valor > conta["saldo"]
    excedeu_limite = valor > limite
    excedeu_saques = conta["saques"] >= limite_saques

    if excedeu_saldo:
        print("\n>>> Saldo insuficiente! <<<")
    elif excedeu_limite:
        print("\n>>> Valor excede o limite de saque. <<<")
    elif excedeu_saques:
        print("\n>>> Número máximo de saques atingido. <<<")
    elif valor > 0:
        conta["saldo"] -= valor
        conta["extrato"] += f"\nSaque: R$ {valor:.2f}"
        conta["saques"] += 1
        print("\n>>> Saque realizado com sucesso! <<<")
    else:
        print("\n>>> Valor inválido. <<<")


def exibir_extrato(contas):
    cpf = input("Informe o CPF do titular: ")
    conta = localizar_conta_por_cpf(cpf, contas)

    if not conta:
        print("\n>>> Conta não encontrada. <<<")
        return

    print("\n=========== EXTRATO ===========")
    print(conta["extrato"] if conta["extrato"] else "Não houve movimentações.")
    print(f"\nSaldo atual: R$ {conta['saldo']:.2f}")
    print("================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")

    usuario_existente = next((u for u in usuarios if u["cpf"] == cpf), None)
    if usuario_existente:
        print("\n>>> CPF já cadastrado! <<<")
        return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (rua, nº - bairro - cidade/estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\n>>> Usuário criado com sucesso! <<<")


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)

    if usuario:
        conta = {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario,
            "saldo": 0,
            "extrato": "",
            "saques": 0
        }
        print("\n>>> Conta criada com sucesso! <<<")
        return conta

    print("\n>>> Usuário não encontrado. <<<")
    return None


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta["agencia"]}
        C/C:\t\t{conta["numero_conta"]}
        Titular:\t{conta["usuario"]["nome"]}
        """
        print(textwrap.dedent(linha))


