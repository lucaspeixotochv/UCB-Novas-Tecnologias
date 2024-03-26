# Escreva um aplicativo que insere um número consistindo em cinco dígitos do usuário, separa o número em seus dígitos individuais e imprime os dígitos separados uns dos outros por três espaços cada. Por exemplo, se o usuário digitar o número 42339, o programa deve imprimir: 4 2 3 3 9.
# Aluno: Lucas Peixoto

numero = int(input("Insira um número inteiro de 5 dígitos: "))
numero = str(numero)
for digito in numero:
    print(digito, end="   ")
print()