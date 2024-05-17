from agenda import Agenda
from contato import Contato

def menu():
    agenda = Agenda()
    while True:
        print("\nAgenda de Contatos")
        print("1. Adicionar contato")
        print("2. Remover contato")
        print("3. Listar contatos")
        print("4. Buscar contato")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            endereco = input("Endereço: ")
            email = input("Email: ")
            contato = Contato(nome, telefone, endereco, email)
            agenda.adicionar_contato(contato)
        
        elif opcao == '2':
            nome = input("Nome do contato a ser removido: ")
            agenda.remover_contato(nome)
        
        elif opcao == '3':
            agenda.listar_contatos()
        
        elif opcao == '4':
            nome = input("Nome do contato a ser buscado: ")
            agenda.buscar_contato(nome)
        
        elif opcao == '5':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
