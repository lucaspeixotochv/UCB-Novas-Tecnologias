# Escreva um programa que leia a quantidade em segundos e imprima o resultado em dias, horas, minutos e segundos.
# Aluno: Lucas Peixoto

segundos = int(input("Insira a quantidade de segundos: "))
dias = segundos // 86400
segundos = segundos % 86400
horas = segundos // 3600
segundos = segundos % 3600
minutos = segundos // 60
segundos = segundos % 60
print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.")
