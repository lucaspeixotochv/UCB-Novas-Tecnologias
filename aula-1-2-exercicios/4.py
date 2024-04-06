def separar_digitos(numero):
    digitos = []
    for digito in str(numero):
        digitos.append(digito)
    return digitos

def main():
    try:
        numero = int(input("Digite um número de cinco dígitos: "))
        if len(str(numero)) != 5:
            print("Por favor, digite um número de cinco dígitos.")
        else:
            digitos = separar_digitos(numero)
            print("Dígitos separados por três espaços:")
            for digito in digitos:
                print(digito, end="   ")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

main()
