pessoa1 = {
    'first_name': 'João',
    'last_name': 'Silva',
    'age': 21,
    'city': 'Brasilia'
}

pessoa2 = {
    'first_name': 'Jade',
    'last_name': 'Santos',
    'age': 29,
    'city': 'Brasilia'
}

pessoa3 = {
    'first_name': 'Carlos',
    'last_name': 'Oliveira',
    'age': 25,
    'city': 'Brasilia'
}

people = [pessoa1, pessoa2, pessoa3]

for pessoa in people:
    print("\nInformações sobre a pessoa:")
    print("Primeiro nome:", pessoa['first_name'])
    print("Sobrenome:", pessoa['last_name'])
    print("Idade:", pessoa['age'])
    print("Cidade:", pessoa['city'])
