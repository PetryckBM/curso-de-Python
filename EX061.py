from math import exp

while True:
    try:
        nr = int(input("digite um numero: "))
        s = nr * 3
        print (s)
        q = 12 / s
        print(q)
        break
    except ValueError:
        print("entre com numero valido")
    except ZeroDivisionError:
        print("divisao por zero!")
    else:
        print("entrou no else")
    finally:
        print("entrou no finally")
    