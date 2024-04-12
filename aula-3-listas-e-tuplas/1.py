lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

maior = max(lista)
print("Maior elemento:", maior)


menor = min(lista)
print("Menor elemento:", menor)


pares = [num for num in lista if num % 2 == 0]
print("Números pares:", pares)

primeiro_elemento = lista[0]
ocorrencias_primeiro = lista.count(primeiro_elemento)
print("Ocorrências do primeiro elemento:", ocorrencias_primeiro)

media = sum(lista) / len(lista)
print("Média dos elementos:", media)

negativos = [num for num in lista if num < 0]
soma_negativos = sum(negativos)
print("Soma dos elementos negativos:", soma_negativos)
