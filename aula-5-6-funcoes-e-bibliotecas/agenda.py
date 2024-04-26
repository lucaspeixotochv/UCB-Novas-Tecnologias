import csv

filename = "agenda.csv"


def ler():
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        return []


def grava(contatos):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(contatos)


def lista(contatos):
    print("\nLista de Contatos:")
    for index, contato in enumerate(contatos, start=1):
        print(
            f"{index}. Nome: {contato[0]}, Telefone: {contato[1]}, Tipo: {contato[2]}, Email: {contato[3]}, Aniversário: {contato[4]}"
        )


def adiciona(contatos):
    nome = input("Nome do contato: ")
    if any(c[0] == nome for c in contatos):
        print("Erro: Já existe um contato com esse nome!")
        return contatos
    telefone = input("Telefone: ")
    tipo = input("Tipo de telefone (celular, fixo, residência, trabalho): ")
    email = input("Email: ")
    aniversario = input("Data de aniversário (dd/mm/aaaa): ")
    contatos.append([nome, telefone, tipo, email, aniversario])
    return contatos


def apaga(contatos):
    nome = input("Nome do contato a ser apagado: ")
    contatos = [c for c in contatos if c[0] != nome]
    return contatos


def altera(contatos):
    nome = input("Nome do contato a ser alterado: ")
    for i, contato in enumerate(contatos):
        if contato[0] == nome:
            novo_nome = input("Novo nome: ")
            novo_telefone = input("Novo telefone: ")
            novo_tipo = input("Novo tipo de telefone: ")
            novo_email = input("Novo email: ")
            novo_aniversario = input("Nova data de aniversário: ")
            contatos[i] = [
                novo_nome,
                novo_telefone,
                novo_tipo,
                novo_email,
                novo_aniversario,
            ]
            break
    else:
        print("Contato não encontrado.")
    return contatos


def ordena(contatos):
    return sorted(contatos, key=lambda x: x[0])


def menu():
    contatos = ler()
    while True:
        print(f"\nAgenda - Total de Contatos: {len(contatos)}")
        print("1 - Listar Contatos")
        print("2 - Adicionar Contato")
        print("3 - Apagar Contato")
        print("4 - Alterar Contato")
        print("5 - Ordenar Contatos por Nome")
        print("6 - Gravar e Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            lista(contatos)
        elif opcao == "2":
            contatos = adiciona(contatos)
        elif opcao == "3":
            contatos = apaga(contatos)
        elif opcao == "4":
            contatos = altera(contatos)
        elif opcao == "5":
            contatos = ordena(contatos)
        elif opcao == "6":
            grava(contatos)
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    menu()