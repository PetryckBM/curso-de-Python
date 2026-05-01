from operator import truediv


def validar_cpf(cpf):
    cpf = "".join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    #culculo do 1 digito verificador

    soma=sum(int(cpf[i]) * (10 - i) for i in range (9))
    resto =  soma%11
    if resto <2:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = 11 - resto

    if int(cpf[9]) != digito_verificador_1:
        return False

    #culculo do 2 digito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range (10))
    resto = soma % 11
    if resto < 2:
        digito_verificador_2 = 0
    else:
        digito_verificador_2 = 11 - resto

    if int(cpf[10]) != digito_verificador_2:
        return False

    return True

cpf = input('digite seu CPF pra ser validado:')

if validar_cpf(cpf):
    print('CPF valido')
else:
    print('CPF invalido')

