class Contato:
    def __init__(self, nome, telefone, endereco, email):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Endereço: {self.endereco}, Email: {self.email}"
