from datetime import date


maior = 0
menor = 0

for a in range (1,8):
    ano = int(input("digite o ano de nacimento: "))
    if (date.today().year - ano) > 18:
        maior +=1
    else:
        menor +=1
print(maior,menor)