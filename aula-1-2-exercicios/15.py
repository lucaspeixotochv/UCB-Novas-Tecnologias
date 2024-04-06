def calcular_quadrado(n):
    quadrado = 0
    numero_impar = 1
    for _ in range(n):
        quadrado += numero_impar
        numero_impar += 2
    return quadrado

def main():
    try:
        n = int(input("Digite um número natural para calcular o seu quadrado: "))
        if n <= 0:
            print("Por favor, digite um número natural válido.")
            return
        resultado = calcular_quadrado(n)
        print(f"O quadrado de {n} é {resultado}.")
    except ValueError:
        print("Por favor, digite um número natural válido.")

main()
