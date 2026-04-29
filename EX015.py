
import random


computador = random.randint(1, 10)

print(computador)

pessoa = int(input("digite um numero de 1 a 10:"))

if computador == pessoa:
    print('voce acertou, parabens!!')
else:
    print('voce errou')