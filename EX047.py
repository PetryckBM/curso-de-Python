n = n2 = tabuada = 0

while True:
    n = int(input("digite um numero pra ver a tabuada: "))
    if n < 0:
        print("programa encerrado!!")
        break
        
    else:
        while n2 <=10:
            tabuada = n * n2
            print(f"{n} X {n2} = {tabuada}")
            n2+=1
    n2 = 0
