a1 = int(input("digite o primero termo: "))
razao = int(input("digite a Razão: "))
termo = a1
cont = 1

while cont <= 10:
    print(f'{termo} ', end = '')
    termo += razao
    cont +=1 