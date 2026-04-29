numero = int(input('digite um numero: '))

if numero <= 200:
    print('sua viagem vai custar: {} reais'.format(numero*0.50))
else:
    print('sua viagem vai custar: {} reais'.format(numero*0.45))