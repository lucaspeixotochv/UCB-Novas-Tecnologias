# Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.
# Aluno: Lucas Peixoto

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def print_first_n_primes(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            print(num, end=" ")
            count += 1
        num += 1

num = int(input("Insira um número: "))
print_first_n_primes(num)
