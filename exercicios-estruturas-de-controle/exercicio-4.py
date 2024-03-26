# Escreva um aplicativo que lê um inteiro não negativo, calcula e imprime seu fatorial.
# Aluno : Lucas Peixoto

def calcular_fatorial(n):
  if n < 0:
    return "Não é possível calcular o fatorial de um número negativo, insira um número positivo."
  elif n == 0:
    return 1
  else:
    fatorial = 1
    for i in range(1, n + 1):
      fatorial *= i
    return fatorial
  
while True:
        num = int(input("Insira um número inteiro não negativo ou -1 para encerrar o programa: "))
        if num == -1:
           break
        resultado = calcular_fatorial(num)
        print(f"O fatorial de {num} é: {resultado}")



