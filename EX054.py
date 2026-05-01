#sequencia de fibonacci

def fibonacci(n):
    if n == 1 or n ==2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("digite o numero da sequencia de fibonacci: "))
sequencia = fibonacci(n)
print(f'o {n} termo da sequancia de fibonacci é: {sequencia}')