

saldo = 0
saque = 0
extrato = []

print("Bem vindo ao Banco MB")

while True:
    print("## Menu Principal ##")
    print("Escolha uma opção: ")
    print("S - Saque")
    print("D - Depósito")
    print("E - Extrato")
    print("S - Saldo")
    print("X - Sair")

    opcao = input("Digite a opção desejada: ").upper()

    if opcao == "S":
        float(input("Opção escolhida = SAQUE\nLimite de R$500,00 por saque\nDigite o valor desejado: R$ "))
        if saldo < saque:
            print("Saldo insuficiente")
            
        else:
            print("Saque realizado com sucesso")




