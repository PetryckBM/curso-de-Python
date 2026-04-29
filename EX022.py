


numero1 = int(input('digite um numero 1: '))
numero2 = int(input('digite um numero 2: '))
numero3 = int(input('digite um numero 3: '))

if numero1 + numero2 > numero3 and numero2 + numero3 > numero1 and numero3 + numero1 > numero2:
    
    if numero1 ==  numero2 == numero3:
        print('trinagulo Equilatero')
    elif numero1 == numero2 != numero3 or numero3 == numero2 != numero1 or numero1 == numero3 != numero2:
        print("triangulo isósceles")
    else:
        print('triangulo escaleno')
else:
    print('nao pode ser um triangular')