import random
palite = 0
computador = random.randint(1, 10)
pessoa = ''

while pessoa != computador:
    pessoa = int(input("digite um numero de 1 a 10: "))
    palite +=1
    if computador == pessoa:
        print(f'voce acertou com {palite} palpites, parabens!!')
    else:
        print('voce errou')