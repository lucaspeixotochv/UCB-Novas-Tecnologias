import math

def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return None, None
    elif delta == 0:
        x = -b / (2*a)
        return x, None
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2

def main():
    try:
        a = float(input("Digite o coeficiente a: "))
        b = float(input("Digite o coeficiente b: "))
        c = float(input("Digite o coeficiente c: "))

        x1, x2 = calcular_raizes(a, b, c)
        if x1 is None and x2 is None:
            print("Não há raízes reais para esta equação.")
        elif x2 is None:
            print(f"A única raiz real é x = {x1}.")
        else:
            print(f"As raízes reais são x' = {x1} e x'' = {x2}.")
    except ValueError:
        print("Por favor, digite coeficientes válidos.")

main()
