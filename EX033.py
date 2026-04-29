a = input("digite a palavra: ").replace(" ","")
inverso = ""
for letro in range (len(a)-1, -1 ,-1):
    inverso +=a[letro]
if inverso == a:
    print('{} é um palindromo'.format(inverso))
else:
    print('nao é um palindromo')

