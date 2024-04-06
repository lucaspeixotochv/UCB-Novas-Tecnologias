def calcular_digito_verificador(numero_conta):
    soma_digitos = sum(int(digito) for digito in str(numero_conta))
    digito_verificador = soma_digitos % 10
    return digito_verificador

def adicionar_digito_verificador(numero_conta):
    digito_verificador = calcular_digito_verificador(numero_conta)
    return f"00{numero_conta}{digito_verificador}"

def main():
    try:
        numero_conta = int(input("Digite o número da conta (sem o dígito verificador): "))
        if numero_conta < 0 or numero_conta > 999999:
            print("Por favor, digite um número de conta válido de até seis dígitos.")
            return
        numero_conta_completo = adicionar_digito_verificador(numero_conta)
        print(f"Número de conta completo: {numero_conta_completo}")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

main()
