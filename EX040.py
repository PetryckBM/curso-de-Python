n1 = int(input("digite um numero: "))
c = n1
resultado = 1
while c > 0:
    resultado = resultado * c
    c -= 1
print(f'o fatorial de {n1} = {resultado}')