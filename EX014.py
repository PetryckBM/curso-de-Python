

nome = input('Digite seu nome completo: ')

nome = nome.split()

print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[-1]))

def imprimir_dados(numero, texto):

    print(f"numero: ",numero)
    print(f"texto: ",texto)

numero1 = 10
texto2 = "Oi Sergio"
imprimir_dados(numero1, texto2)
