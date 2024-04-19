def comparar_listas(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    
    comuns = conjunto1.intersection(conjunto2)
    
    apenas_na_primeira = conjunto1 - conjunto2
    
    apenas_na_segunda = conjunto2 - conjunto1
    
    nao_repetidos = list(conjunto1.union(conjunto2))
    
    sem_repetidos_na_segunda = list(conjunto1 - conjunto2)
    
    return comuns, apenas_na_primeira, apenas_na_segunda, nao_repetidos, sem_repetidos_na_segunda

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

resultado_a, resultado_b, resultado_c, resultado_d, resultado_e = comparar_listas(lista1, lista2)

print("Valores comuns às duas listas:", resultado_a)
print("Valores que só existem na primeira lista:", resultado_b)
print("Valores que existem apenas na segunda lista:", resultado_c)
print("Lista com elementos não repetidos das duas listas:", resultado_d)
print("Primeira lista sem elementos repetidos na segunda lista:", resultado_e)
