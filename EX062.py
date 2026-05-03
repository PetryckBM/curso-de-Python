import tkinter as tk
from tkinter import messagebox
#criando a função de divisao
def dividir_numeros():
    
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 / num2
        messagebox.showinfo("Resultado", f"A divisao dos números é: {resultado}")
            
    except ValueError:
        messagebox.showerror("Error", "Por favor. insira números válidos.")

    except ZeroDivisionError:
        messagebox.showerror("Error", "Divisão por Zero!!.")
       

# Criando a janela
janela = tk.Tk()
janela.title("Calculadora de Divisao")

# Criando os widgets
label_num1 = tk.Label(janela, text="Número 1:")
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_num1 = tk.Entry(janela)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(janela, text="Número 2:")
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_num2 = tk.Entry(janela)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

botao_somar = tk.Button(janela, text="Dividir", command=dividir_numeros)
botao_somar.grid(row=2, columnspan=2, padx=10, pady=5)

# Rodando o loop principal
janela.mainloop()