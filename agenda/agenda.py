from contato import Contato

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato: Contato):
        self.contatos.append(contato)
        print(f"Contato {contato.nome} adicionado com sucesso.")

    def remover_contato(self, nome: str):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                print(f"Contato {nome} removido com sucesso.")
                return
        print(f"Contato {nome} não encontrado.")

    def listar_contatos(self):
        if not self.contatos:
            print("A agenda está vazia.")
        else:
            for contato in self.contatos:
                print(contato)

    def buscar_contato(self, nome: str):
        for contato in self.contatos:
            if contato.nome == nome:
                print(contato)
                return
        print(f"Contato {nome} não encontrado.")
