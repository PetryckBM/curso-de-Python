import tkinter as tk
from tkinter import messagebox

def compador_numeros():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    
    if num1 > num2:
        messagebox.showinfo("resultado",f"dos dois numero escolhidos os {num1} é maior")
    elif num2 > num1:
        messagebox.showinfo("resultado",f"dos dois numero escolhidos os {num2} é maior")
    elif num1 == num2:
        messagebox.showinfo("resultado",f"Os dois numeros são iguais")

# Criando a janela
janela = tk.Tk()
janela.title("Comparador de numeros")

# Criando os widgets
label_num1 = tk.Label(janela, text="Número 1:")
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_num1 = tk.Entry(janela)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(janela, text="Número 2:")
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_num2 = tk.Entry(janela)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

botao_somar = tk.Button(janela, text="Comparar", command=compador_numeros)
botao_somar.grid(row=2, columnspan=2, padx=10, pady=5)

# Rodando o loop principal
janela.mainloop()