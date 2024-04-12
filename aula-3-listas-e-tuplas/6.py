lugares_vagos = [10, 2, 1, 3, 0]

while True:
    sala = int(input("Digite o número da sala (ou 0 para sair): "))

    if sala == 0:
        print("Programa encerrado.")
        break

    if sala < 1 or sala > len(lugares_vagos):
        print("Sala inválida. Digite um número de sala válido.")
        continue

    lugares_solicitados = int(input("Digite a quantidade de lugares desejados: "))

    if lugares_vagos[sala - 1] >= lugares_solicitados:
        lugares_vagos[sala - 1] -= lugares_solicitados
        print("Bilhetes vendidos com sucesso!")
    else:
        print("Desculpe, não há lugares suficientes disponíveis.")

    print("Situação atual das salas:", lugares_vagos)
