def verificar_paridade(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

def main():
    try:
        numero = int(input("Digite um número inteiro: "))
        paridade = verificar_paridade(numero)
        print(f"O número {numero} é {paridade}.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

main()
