
saldo = 0
saque_limite = 0
extrato = []

print("\nBem vindo ao MBank\n")

while True:
    print("## Menu Principal ##\n")
    print("Escolha uma opção: ")
    print("S - Saque")
    print("D - Depósito")
    print("E - Extrato")
    print("X - Sair\n")

    opcao = input("Digite a opção desejada: ").upper()

    # SAQUE
    if opcao == "S":
        if saque_limite >= 3:
            print("\n>>> Limite de saque atingido <<<")
        else:
            saque = float(input("\nOpção escolhida = SAQUE\nLimite de R$500,00 por saque\nDigite o valor desejado: R$"))
            
            if saldo < saque:
                print(">>> Saldo insuficiente <<<")
            elif saque > 500:
                print("\nValor do saque excede o limite de R$500,00")
            else:
                saldo -= saque
                saque_limite += 1
                extrato.append(f"Saque de R$ {saque:.2f}")
                print("\nSaque realizado com sucesso")
            print(f">>> \nSaldo atualizado: R$ {saldo:.2f}")
        
    # DEPÓSITO
    elif opcao == "D":
        deposito = float(input("\nOpção escolhida = DEPÓSITO\nDigite o valor a depositar: R$"))
        if deposito <= 0:
            print("\n>>> Valor inválido <<<")
        else:
            saldo += deposito
            extrato.append(f"\nDepósito de R$ {deposito:.2f}")
            print(f"\n>>> Saldo atualizado: R$ {saldo:.2f}")

    # EXTRATO
    elif opcao == "E":
        if not extrato:
            print("\n>>> Nenhuma transação realizada <<<")
            print(f">>> Saldo atualizado: R$ {saldo:.2f}")

        else:
            print("\nExtrato:")
            for item in extrato:
                print(item)
            print(f"\n>>> Saldo atualizado: R$ {saldo:.2f}")

    elif opcao == "X":
        print("\n>>> Sessão encerrada <<<")
        break

    else:
        print("\n>>> Opção inválida <<<")   
    

    
    
    




