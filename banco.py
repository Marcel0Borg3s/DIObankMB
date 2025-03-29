saldo = 0
saque_limite = 0
extrato = []

# Definindo a função SACAR
def sacar(valor):
    global saldo, saque_limite

    if valor <= 0:
        return "\n>>>Valor inválido<<<\n"
    elif valor > 500:
        return "\n>>>Valor superior ao limite!<<<\n"
    elif saque_limite >= 3:
        return "\n>>>Limite de saque diário ultrapassado!<<<\n"
    elif saldo < valor:
        return "\n>>>Saldo insuficiente!<<<\n"
    else:
        saldo -= valor
        saque_limite += 1
        extrato.append(f'\nSaque realizado no valor de R${valor:.2f}\n')
        return "\nSaque realizado com sucesso!\n"

# Definindo a função DEPOSITAR
def depositar(deposito):
    global saldo

    if deposito <= 0:
        return "\n>>>Valor inválido<<<\n"
    else:
        saldo += deposito
        extrato.append(f'\nDepósito realizado de R${deposito:.2f}\n')
        return "\nDepósito realizado com sucesso!\n"

# Definindo a função EXTRATO
def extrato_geral():
    global extrato
    if not extrato:
        return "\nNenhuma transação realizada.\n"
    else:
        resultado = "\n>>>Extrato<<<\n"
        for item in extrato:
            resultado += f"{item}\n"
        return resultado



