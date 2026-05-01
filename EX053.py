

def acharnumero(lista):  
    return max(lista)

lista = int(input('digite um numero: '))
while lista != 999:
    lista.append(int(input('digite um numero: ')))
    if lista[-1] == 999:
        break
acharnumero(lista)
print(acharnumero(lista))
print(f'a quantidade de numeros digitados foi {len(lista)}')