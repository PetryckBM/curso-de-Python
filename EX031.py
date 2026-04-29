a1 = int(input("digite o primero termo"))
razao = int(input("digite a Razão"))

razao  = razao - a1

for termo in range (1,11):
    a10 = a1+(termo - 1)*3
    print('a progessão aritimetica é :{}'.format(a10))

