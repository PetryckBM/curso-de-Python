numero1 = int(input('digite um numero 1: '))
numero2 = int(input('digite um numero 2: '))
numero3 = int(input('digite um numero 3: '))

if numero3 > numero2 and numero1:
    print('o numero 3 é o maior')
elif numero2 > numero1 and numero3:
    print('o numero 2 é o maior')
else:
     print('o numero 1 é o maior')