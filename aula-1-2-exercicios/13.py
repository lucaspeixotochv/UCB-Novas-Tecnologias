def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

def main():
    try:
        n = int(input("Digite um número inteiro não negativo para calcular o fatorial: "))
        if n < 0:
            print("Por favor, digite um número inteiro não negativo.")
            return
        resultado = calcular_fatorial(n)
        print(f"O fatorial de {n} é {resultado}.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

main()

