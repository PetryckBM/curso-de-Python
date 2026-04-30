idade  = n1 = n2= n3 =1
teste = sexo = ''
while True:
    idade = int(input("Digite sua Idade: "))
    sexo = str(input("Digite sua Sexo [F/M]: ")).upper()
    while sexo not in 'MF':
        sexo = str(input("Digite sua Sexo [F/M]: ")).upper()

    teste = str(input("Quer continuar[S/N]?")).upper()
    if teste == "N":
        print("Fim do programa!!")
        break
    else:
        if idade > 17:
            n1 +=1
            if sexo == "M":
                n2 +=1
                if sexo == 'F' and idade >= 20:
                    n3 +=1
print(f"A quantidade de pessoas maior de 18 anos foram {n1}!")
print(f"A quantidade de homens foram {n2}!")
print(f"A quantidade de mulheres com mais de 20 anos foram {n3}!")
