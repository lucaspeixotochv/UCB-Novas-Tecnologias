def adicao_tabuada():
    numero = int(input("Digite o número para a tabuada de adição: "))
    print(f"Tabuada de adição para o número {numero}:")
    for i in range(1, 11):
        resultado = numero + i
        print(f"{numero} + {i} = {resultado}")

def subtracao_tabuada():
    numero = int(input("Digite o número para a tabuada de subtração: "))
    print(f"Tabuada de subtração para o número {numero}:")
    for i in range(1, 11):
        resultado = numero - i
        print(f"{numero} - {i} = {resultado}")

def multiplicacao_tabuada():
    numero = int(input("Digite o número para a tabuada de multiplicação: "))
    print(f"Tabuada de multiplicação para o número {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def divisao_tabuada():
    numero = int(input("Digite o número para a tabuada de divisão: "))
    print(f"Tabuada de divisão para o número {numero}:")
    for i in range(1, 11):
        if i != 0:
            resultado = numero / i
            print(f"{numero} ÷ {i} = {resultado}")
        else:
            print(f"Não é possível dividir por zero.")

def main():
    while True:
        print("\nMenu:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicao_tabuada()
        elif opcao == "2":
            subtracao_tabuada()
        elif opcao == "3":
            multiplicacao_tabuada()
        elif opcao == "4":
            divisao_tabuada()
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Escolha novamente.")

main()
