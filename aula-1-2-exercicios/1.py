num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2
print("A soma dos números é:", soma)

produto = num1 * num2
print("O produto dos números é:", produto)

diferenca = num1 - num2
print("A diferença dos números é:", diferenca)

if num2 != 0:
    divisao = num1 / num2
    print("A divisão dos números é:", divisao)
else:
    print("Não é possível dividir por zero.")
