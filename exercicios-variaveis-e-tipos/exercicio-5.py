# Escreva um aplicativo que receba a, b e c, coeficientes de uma equação do segundo grau, e calcule as raízes x’ e x” através da fórmula de Báskara.
# Aluno: Lucas Peixoto

a = float(input("Insira o coeficiente a: "))
b = float(input("Insira o coeficiente b: "))
c = float(input("Insira o coeficiente c: "))

delta = (b ** 2) - (4 * a * c)

if delta < 0:
    print("A equação não possui raízes reais.")
else:
    x1 = (-b + (delta ** 0.5)) / (2 * a)
    x2 = (-b - (delta ** 0.5)) / (2 * a)
    print(f"As raízes da equação são: x1 = {x1} e x2 = {x2}")
