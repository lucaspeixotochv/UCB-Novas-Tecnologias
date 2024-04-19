animal1 = {'nome': 'Fido', 'tipo': 'cachorro', 'dono': 'João'}
animal2 = {'nome': 'Whiskers', 'tipo': 'gato', 'dono': 'Maria'}
animal3 = {'nome': 'Nemo', 'tipo': 'peixe', 'dono': 'Carlos'}

pets = [animal1, animal2, animal3]

for animal in pets:
    print("\nInformações sobre o animal de estimação:")
    print("Nome:", animal['nome'])
    print("Tipo:", animal['tipo'])
    print("Dono:", animal['dono'])
