# Classe Livro
class Livro:
    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade


# Questão 1: Criação da classe Pessoa

class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'

    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        return f'Olá, eu sou {self.nome} e trabalho como {self.profissao}.'

pessoa = Pessoa('João', 30, 'Engenheiro')
print(pessoa)  
print(pessoa.saudacao)  
pessoa.aniversario()


# Questão 2, 3, 4 e 5: Criação da classe ContaBancaria

class ContaBancaria:
    def __init__(self, titular='', saldo=0.0):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Conta de {self.titular} - Saldo: R$ {self.saldo:.2f}'

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

    @ativo.setter
    def ativo(self, valor):
        self._ativo = valor

    @classmethod
    def ativar_conta(cls, conta):
        conta.ativo = True

conta1 = ContaBancaria('Maria', 1000.0)
conta2 = ContaBancaria('Pedro', 2000.0)
print(conta1)  
print(conta2)  

conta3 = ContaBancaria('Ana', 1500.0)
ContaBancaria.ativar_conta(conta3)
print(conta3.ativo)  # True

conta4 = ContaBancaria('Carlos', 3000.0)
print(conta4.titular)  # Carlos


# Questão 7 e 8: Criação da classe ClienteBanco e método de classe

class ClienteBanco:
    def __init__(self, nome, cpf, endereco, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    @classmethod
    def criar_cliente(cls, nome, cpf, endereco, telefone, email):
        return cls(nome, cpf, endereco, telefone, email)

cliente1 = ClienteBanco('Alice', '111.111.111-11', 'Rua Marechal, 123', '1111-1111', 'alice@example.com')
cliente2 = ClienteBanco('Marcos', '222.222.222-22', 'Rua XV, 456', '2222-2222', 'marcos@example.com')
cliente3 = ClienteBanco('Diogo', '333.333.333-33', 'Rua Visconde, 789', '3333-3333', 'diogo@example.com')
print(cliente3.nome, cliente.cpf, cliente4.endereco, cliente4.telefone, cliente4.email)  # David
