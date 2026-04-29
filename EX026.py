
from datetime import date


ano = int(input('digite data de nacimento '))

ano = date.today().year - ano

if ano <=9:
    print("mirim")
elif ano <=14:
    print("infantil")
elif ano <=19:
    print("junior")
elif ano <= 20:
    print("senior")
else:
    print("master")
