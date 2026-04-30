n = cont =soma =0

while n != 999:
    n = int(input("digite um numero de 1 a 999: "))
    if n !=999:
        cont +=1
        soma +=n
print(f'a quantidade de numero digitados foi {cont} e o a soma foi {soma}')