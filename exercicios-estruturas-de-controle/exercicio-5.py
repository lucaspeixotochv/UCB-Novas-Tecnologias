# O quadrado de um número natural n é dado pela soma dos n primeiros números ímpares consecutivos. Por exemplo, 1^2 1, 2^2  13 etc. Dado um número n, calcule seu quadrado usando a soma de ímpares ao invés de produto.
# Aluno: Lucas Peixoto

def calular_quadrado(n):
  if n <= 0:
    return "O número deve ser um número natural positivo."
  
  quadrado = 0
  numero_impar = 1
  for i in range(n):
    quadrado += numero_impar
    numero_impar += 2

  return quadrado

while True:
  num = int(input("Insira um número natural ou 0 para encerrar o programa: "))
  if num == 0:
    break
  resultado = calular_quadrado(num)
  print(f"O quadrado de {num} é: {resultado}")