


n2 = int(input("digite um numero de sequencias: "))
t1 = 0
t2 = 1
cont = 3
print(f'a sequencia e {t1}')
print(f'a sequencia e {t2}')
while cont <= n2:
    sequencia = t1 + t2
    t1 = t2
    t2 = sequencia
    cont +=1
    print(f'a sequencia e {sequencia}')
print('fim!')