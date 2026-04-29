soma = 0

for s in range(0,6):
    n = int(input("digite um numero:"))
    if n % 2 == 0:
        soma += n 

print("a soma dos pares é {}".format(soma))