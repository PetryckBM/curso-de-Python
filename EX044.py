
n1 = 0
n3=0
n2=0
while n1 != 999:
    n1 = int(input("digite um numero de 1 a 999: "))
    if n1 != 999:
        n2 = n2 + 1
        n3 = n3 + n1
print(f'a quantidades de tentativas foram {n2} e a soma das tentativas foram {n3}')