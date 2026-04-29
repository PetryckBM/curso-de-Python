n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
resultado =0
print('digite [1] soma, [2] multiplicar, [3] maior, [4] novos numeros, [5] sair do programa')
opcao = 0

while opcao !=  5:
    opcao = int(input("digite novamente"))
    if opcao == 1:
        resultado = n1 + n2
        print(f'o resultado da soma e {resultado}')

    if opcao == 2:
        resultado = n1 * n2
        print(f'o resultado da multiplicao e {resultado}')

    if opcao == 3:
        if n1 > n2:
            print(f'nuemro 1 e maior')
        else:
            print(f'nuemro 2 e maior')
    if opcao == 4:
        n1 = int(input('digite um numero 1: '))
        n2 = int(input('digite um numero 2: '))
    if opcao == 5:
        print('voce saiu do programa!!')
    
            
