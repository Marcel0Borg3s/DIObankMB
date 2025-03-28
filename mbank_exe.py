import tkinter as tk

def conta_bancaria():
    print("Acionando a função da def Conta Bancária")


def mbank_window():
    window = tk.Tk()
    window.title("*****MBank*****")
    window.geometry("400x600")
   

    # Mensagem de abertura
    label = tk.Label(window, text="Bem vindo ao MBank!", font=("Arial", 14, "bold"), fg="blue")
   
    # Criando um espaço superior para mensagem
    label.pack(pady=20)

    # Chamando o Menu de opções
    label = tk.Label(window, text="Menu principal", font=("Arial", 12, "bold"))
    label.pack(pady=10)
    
    # inclusão dos botões de opções
    # Saque
    btn_saque = tk.Button(window, text="Saque", font=("Arial", 12), width=15, bg="blue", fg="white", command=conta_bancaria)
    btn_saque.pack(pady=5)
    # Depósito
    btn_deposito = tk.Button(window, text="Depósito", font=("Arial", 12), width=15, bg="blue", fg="white", command=conta_bancaria)
    btn_deposito.pack(pady=5)
    # Extrato
    btn_extrato = tk.Button(window, text="Extrato", font=("Arial", 12), width=15, bg="blue", fg="white", command=conta_bancaria)
    btn_extrato.pack(pady=5)
    # Sair
    btn_sair = tk.Button(window, text="Sair", font=("Arial", 12), width=15, bg="blue", fg="white", command=window.quit)
    btn_sair.pack(pady=5)










    window.mainloop()

mbank_window()