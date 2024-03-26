# A série de Fibonacci é 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Os dois primeiros termos são iguais a 1, e a partir do terceiro, o termo é dado pela soma dos dois termos anteriores. Dado um número n≥ 3, exiba o n-ésimo termo da série de Fibonacci.
# Aluno: Lucas Peixoto

def fibonacci(n):
    if n <= 0:
        return "N deve ser um número inteiro positivo."
    
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    
    fibonacci = [1, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    return fibonacci

n = int(input("Digite o valor de n (n >= 3): "))
resultado = fibonacci(n)

print(f"Os primeiros {n} termos da série de Fibonacci são: {resultado}")