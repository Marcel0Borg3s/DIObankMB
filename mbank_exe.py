import tkinter as tk
from banco import sacar, depositar, extrato_geral

# Configuração para chamar a função banco
def acionar_saque():
    valor_str = entry_valor.get() #capturar valor digitado
    try:
        valor = float(valor_str)
        resultado = sacar(valor)
        label_resultado.config(text=resultado)
    except ValueError:
        label_resultado.config(text="Digite um valor válido!")

def acionar_deposito():
    valor_str = entry_valor.get() #capturar valor digitado
    try:
        valor = float(valor_str)
        resultado = depositar(valor)
        label_resultado.config(text=resultado)
    except ValueError:
        label_resultado.config(text="Digite um valor válido!")

def exibir_extrato():
    resultado = extrato_geral()
    label_resultado.config(text=resultado)

# Configuração para a interface
def mbank_window():
    global entry_valor, label_resultado

    window = tk.Tk()
    window.title("***** M B A N K *****")
    window.geometry("400x600")
   

    # Mensagem de abertura
    label = tk.Label(window, text="Bem vindo ao MBank!", font=("Arial", 14, "bold"), fg="blue")
   
    # Criando um espaço superior para mensagem
    label.pack(pady=20)

    # Chamando o Menu de opções
    label = tk.Label(window, text="Menu principal", font=("Arial", 12, "bold"))
    label.pack(pady=10)

    # Criando a label para exibição dos resultados
    label_resultado = tk.Label(window, text="", font=("Arial", 12), fg="red")
    label_resultado.pack(pady=10)

    # Criando o Label e entrada de valores
    label_valor = tk.Label(window, text="Digite o valor: ", font=("Arial", 12))
    label_valor.pack(pady=5)

    # Criando a entrada de valores
    entry_valor = tk.Entry(window, font=("Arial", 12))
    entry_valor.pack(pady=5)

    # inclusão dos botões de opções
    # Saque
    btn_saque = tk.Button(window, text="Saque", font=("Arial", 12), width=15, bg="blue", fg="white", command=acionar_saque)
    btn_saque.pack(pady=5)
    # Depósito
    btn_deposito = tk.Button(window, text="Depósito", font=("Arial", 12), width=15, bg="blue", fg="white", command=acionar_deposito)
    btn_deposito.pack(pady=5)
    # Extrato
    btn_extrato = tk.Button(window, text="Extrato", font=("Arial", 12), width=15, bg="blue", fg="white", command=exibir_extrato)
    btn_extrato.pack(pady=5)
    # Sair
    btn_sair = tk.Button(window, text="Sair", font=("Arial", 12), width=15, bg="blue", fg="white", command=window.quit)
    btn_sair.pack(pady=5)


    window.mainloop()

mbank_window()