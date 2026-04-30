import random


jogador = computador = count =0

while True:
    jogador = int(input("digite um valor: "))
    jogada = str(input("Par oi Ímpar? [P/I]"))
    computador = random.randint(1,10)
    resultado = jogador + computador 

    if jogada == 'P' and resultado %2 != 0 or jogada == 'I' and resultado %2 == 0:
        print(f'voce jogou {jogador} e o computador {computador}. Total de {resultado}.')
        print("voce perdeu!")
        break
    else:
        count+=1
        print("Voce venceu!!")
print(f"Game Over! Voce venceu {count} vezes.")
