# Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida. Repita até que a opção saída seja escolhida.
# Aluno : Lucas Peixoto


num1 = int(input("Entre com um número: "))
num2 = int(input("Entre com outro numero: "))
ope = 1
while ope!=0:
    ope = int(input("Digite a operação desejada\n \
      1- Soma\n \
      2- Subtração\n \
      3- Multiplicação\n \
      4 - Divisão \n \
      0 - Para sair \n"))
    if ope==1:
        print(f"A soma de {num1}+{num2}={num1+num2} \n")
    elif ope==2:
        print(f"A subtração de {num1}-{num2}={num1-num2}\n")
    elif ope==3:
        print(f"A soma de {num1}x{num2}={num1*num2} \n")
    elif ope==4:
        print(f"A soma de {num1}/{num2}={num1/num2} \n")
    else:
        print("Opção inválida")