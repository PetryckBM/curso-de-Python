a1 = int(input("digite o primero termo: "))
razao = int(input("digite a Razão: "))
ultimo = int(input("digite ate quanto gostaria de ir: "))
termo = a1
cont = 1
mais = 0
while ultimo != 0:
    ultimo = ultimo + mais
    while cont <= ultimo:
        print(f'{termo} ', end = '')
        termo += razao
        cont +=1
    mais = int(input('quantos termoas voce quer mostrar a mais? '))
        
