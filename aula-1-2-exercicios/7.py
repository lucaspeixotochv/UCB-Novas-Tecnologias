def converter_segundos(segundos):
    dias = segundos // (24 * 3600)
    segundos = segundos % (24 * 3600)
    horas = segundos // 3600
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60
    return dias, horas, minutos, segundos

def main():
    try:
        segundos = int(input("Digite a quantidade de segundos: "))
        dias, horas, minutos, segundos_restantes = converter_segundos(segundos)
        print(f"{segundos} segundos equivalem a:")
        print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

main()
