


soma = count = contador =menor=0
barato=""

while True:
    nome = str(input('digite o nome do produto:'))
    preco = int(input('digite o preço do produto: '))
    teste = str(input("Quer continuar[S/N]?")).upper().strip()[0]
    contador +=1
    soma +=preco
    
    if preco > 1000:
        count +=1

    if contador ==1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome

    while teste not in 'SN':
        teste = str(input("Quer continuar[S/N]?")).upper().strip()[0]

    if teste == 'N':
        print("Fim do programa!!")
        break    
    

print(f"o total gsto na compra foi {soma}")
print(f"A quantidade de produtos que custam mais de R$ 1000 é {count}")
print(f"o produto mais batato é {barato} que custa {menor:.2f}")
