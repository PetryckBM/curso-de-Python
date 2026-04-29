s = ''
n1 = 0
conta = 0
soma = 0
maior = menor = 0
while s != 'nao':
    n1 = int(input("digite um valor:"))
    soma+=n1
    conta += 1
    if conta  == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    s = str(input('Quer continue?')).lower().strip()
media = soma / conta
print(f'a media e {media}')
print(f'a o total de numeros digitados foram {conta}')
print(f'o maior numero e {maior}')
print(f'o menor numero e {menor}')
