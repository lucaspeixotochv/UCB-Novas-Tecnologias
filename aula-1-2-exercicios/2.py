def exibir_forma(forma):
    for linha in forma:
        print(linha)

def main():
    caixa = [
        "*****",
        "*   *",
        "*   *",
        "*   *",
        "*****"
    ]

    oval = [
        " *** ",
        "*   *",
        "*   *",
        "*   *",
        " *** "
    ]

    seta = [
        "  *  ",
        " *** ",
        "*****",
        "  *  ",
        "  *  "
    ]

    losango = [
        "  *  ",
        " *** ",
        "*****",
        " *** ",
        "  *  "
    ]

    print("Caixa:")
    exibir_forma(caixa)
    print("\nOval:")
    exibir_forma(oval)
    print("\nSeta:")
    exibir_forma(seta)
    print("\nLosango:")
    exibir_forma(losango)

if __name__ == "__main__":
    main()
