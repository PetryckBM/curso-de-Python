


from datetime import date


ano = int(input('digite data de nacimento '))

ano = date.today().year - ano

if ano < 18:
    print("nao precisa se alistar e falta {} pra voce se alistar".format(18 - ano))
elif ano == 18:
    print("esta na hora de se alistar")
else:
    print("Ja passou da hora de se alistar e ja passou {} do prazo".format(ano - 18))
