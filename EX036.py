media = 0
conta = 0
nome1 = []
idade1 = []
sexo1 = []
for pessoas in range(1,5):
    nome = [input('Digite seu nome:')]
    idade = [int(input('digite sua idade: '))]
    sexo = [input('digite seu sexo com F ou M:')]
    nome1 += nome
    idade1 += idade
    sexo1 +=sexo
media = sum(idade1)/ len(idade1)
print(f'a media de idade do grupo é{media}')
if nome1[pessoas] == sexo1[m]:
    print('essas pessoas sao do sexo ')
