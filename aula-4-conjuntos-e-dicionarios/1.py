def contar_caracteres(frase):
    contagem = {}
    for caractere in frase:
        caractere = caractere.lower()
        if caractere.isalpha():
            if caractere in contagem:
                contagem[caractere] += 1
            else:
                contagem[caractere] = 1
    return contagem

frase = input("Digite uma frase: ")
resultado = contar_caracteres(frase)
print(resultado)
