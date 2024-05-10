from datetime import datetime

class ContaBancaria:
    def __init__(self, numero_agencia, tipo_conta, saldo, titular, limite):
        self.numero_agencia = numero_agencia
        self.tipo_conta = tipo_conta
        self.saldo = saldo
        self.limite = limite
        self.titular = titular
        self.historico = Historico()
    
    def consultar_saldo(self):
        return self.saldo
    
    def saca(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.historico.transacoes.append(f"Saque: R${valor} - {datetime.now()}")
        else:
            print("Saldo insuficiente para saque.")
    
    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f"Depósito: R${valor} - {datetime.now()}")
    
    def transfere_para(self, destino, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            destino.saldo += valor
            self.historico.transacoes.append(f"Transferência para {destino.numero_agencia}: R${valor} - {datetime.now()}")
            destino.historico.transacoes.append(f"Transferência de {self.numero_agencia}: R${valor} - {datetime.now()}")
        else:
            print("Saldo insuficiente para transferência.")
    
    def obter_extrato(self):
        self.historico.imprime()
    
    def alterar_titular(self, novo_titular):
        self.titular = novo_titular
        print("Titular da conta alterado com sucesso.")
        pass
    
    def fechar_conta(self):
        self.titular.saldo += self.saldo
        self.saldo = 0
        print("Conta fechada. Saldo transferido para o titular.")
    
class Historico:
    def __init__(self):
        self.data_da_abertura = datetime.now()
        self.transacoes = []
    
    def imprime(self):
        print("Transações realizadas:")
        for transacao in self.transacoes:
            print(transacao)

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
    
    def dados_cliente(self):
        return f"Nome: {self.nome} {self.sobrenome}\nCPF: {self.cpf}"

class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_agencia, tipo_conta, saldo, limite, aniversario_conta):
        super().__init__(numero_agencia, tipo_conta, saldo, limite)
        self.aniversario_conta = aniversario_conta
    
    def calcular_juros_mensal(self, taxa_juros):
        hoje = datetime.now()
        if hoje.day == self.aniversario_conta.day:  
            juros = self.saldo * taxa_juros
            self.saldo += juros
            self.historico.transacoes.append(f"Juros de poupança aplicados: R${juros} - {hoje}")
            return juros
        return 0

class ContaCorrente(ContaBancaria):
    def __init__(self, numero_agencia, tipo_conta, saldo, limite, cheque_especial):
        super().__init__(numero_agencia, tipo_conta, saldo, limite)
        self.cheque_especial = cheque_especial
    
    def utilizar_cheque_especial(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.transacoes.append(f"Utilização de cheque especial: R${valor} - {datetime.now()}")
        else:
            print("Saldo insuficiente para utilizar o cheque especial.")
