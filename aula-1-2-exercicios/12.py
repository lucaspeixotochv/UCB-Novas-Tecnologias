def verificar_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def primeiros_n_primos(n):
    primos_encontrados = 0
    numero = 2
    while primos_encontrados < n:
        if verificar_primo(numero):
            print(numero, end=" ")
            primos_encontrados += 1
        numero += 1

def main():
    try:
        n = int(input("Digite um número inteiro positivo para encontrar os primeiros números primos: "))
        if n <= 0:
            print("Por favor, digite um número positivo.")
            return
        print(f"Os primeiros {n} números primos são:")
        primeiros_n_primos(n)
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

main()
