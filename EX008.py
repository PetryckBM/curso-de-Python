print('calculadora de desconto')

numero1 = int(input("Digite o numero: "))
desconto = input("Quanto de desconto deseja? ")

match desconto:
    case "5":
        print(numero1 * 0.95)
    case "10":
        print(numero1 * 0.90)
    case "20":
        print(numero1 * 0.80)
    case _:
        print("Operação inválida") 
