# Numa certa agência bancária, as contas são identificadas por números de até seis dígitos seguidos de um dígito verificador, calculado conforme exemplificado a seguir. Dado um número de conta n, exiba o número de conta completo correspondente. Seja n  7314 o número da conta. Adicionamos os dígitos de n e obtemos a soma s  4137  15; Calculamos o resto da divisão de s por 10 e obtemos o dígito d  5. Número de conta completo: 0073145
# Aluno: Lucas Peixoto

def calcular_digito_verificador(numero_conta):
    soma = sum(int(digito) for digito in str(numero_conta))
    resto = soma % 10
    digito_verificador = 10 - resto
    return digito_verificador

def numero_conta_completo(numero_conta):
    digito_verificador = calcular_digito_verificador(numero_conta)
    return f"{numero_conta:06d}-{digito_verificador}"

numero_conta = int(input("Digite o número da conta (até 6 dígitos): "))
numero_completo = numero_conta_completo(numero_conta)
print(f"Número de conta completo: {numero_completo}")
