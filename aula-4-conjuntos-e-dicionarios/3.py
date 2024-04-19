def comparar_listas_versao_inicial_e_alterada(inicial, alterada):
    conjunto_inicial = set(inicial)
    conjunto_alterada = set(alterada)
    
    nao_modificados = conjunto_inicial.intersection(conjunto_alterada)
    
    novos_elementos = conjunto_alterada - conjunto_inicial
    
    removidos = conjunto_inicial - conjunto_alterada
    
    return list(nao_modificados), list(novos_elementos), list(removidos)

lista_inicial = [1, 2, 3, 4, 5]
lista_alterada = [1, 3, 5, 6, 7]

nao_modificados, novos_elementos, removidos = comparar_listas_versao_inicial_e_alterada(lista_inicial, lista_alterada)

print("Elementos que não mudaram:", nao_modificados)
print("Novos elementos:", novos_elementos)
print("Elementos removidos:", removidos)
