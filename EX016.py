
velociade = int(input("digite a valocidade do carro: "))

if velociade > 80:
    print('voce foi multado em {} reais'.format((velociade - 80) * 7))
else:
    print('esta tudo certo!!')