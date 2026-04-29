casa = int(input('qual o valor da casa? '))
anos = int(input('quantos anos voce quer pagar? '))
salario = int(input('qual seu salario? '))


prestacao = (casa / anos) / 12

if prestacao > salario * 0.30:
    print("emprestimo negado")
else:
    print("emprestimo aprovado")

print("o valor da prestação é {:0.1f}".format(prestacao))

