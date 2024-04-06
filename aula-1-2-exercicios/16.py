def fibonacci(n):
    if n <= 0:
        return "Por favor, insira um número maior ou igual a 1 para calcular o termo da série de Fibonacci."
    elif n == 1 or n == 2:
        return 1
    else:
        fib = [0] * (n + 1)
        fib[1] = 1
        fib[2] = 1
        for i in range(3, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        return fib[n]

def main():
    try:
        n = int(input("Digite um número maior ou igual a 3 para calcular o n-ésimo termo da série de Fibonacci: "))
        resultado = fibonacci(n)
        print(f"O {n}-ésimo termo da série de Fibonacci é {resultado}.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

main()
