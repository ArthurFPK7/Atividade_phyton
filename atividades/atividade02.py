# Questão 1
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f"Carro: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}"

# Questão 2, 3, 4
class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.endereco = "Desconhecido"
        self.capacidade = 0

    def __str__(self):
        return f"Restaurante: {self.nome}, Categoria: {self.categoria}, Ativo: {self.ativo}, Endereço: {self.endereco}, Capacidade: {self.capacidade}"

# Questão 5
class Cliente:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

    def __str__(self):
        return f"Cliente: {self.nome}, Idade: {self.idade}, Email: {self.email}, Telefone: {self.telefone}"



meu_carro = Carro('Civic', 'Preto', 2020)

# Consumindo o objeto
print(vars(meu_carro))
print(meu_carro)
print('')

restaurante_exemplo = Restaurante('Bistrô Elegante', 'Francesa')

print(vars(restaurante_exemplo))
print(restaurante_exemplo)
print('')

restaurante_novo = Restaurante('Cantina Italiana', 'Italiana')

print(restaurante_novo)
print('')

cliente1 = Cliente('João', 30, 'joao@email.com', '1234-5678')
cliente2 = Cliente('Maria', 25, 'maria@email.com', '8765-4321')
cliente3 = Cliente('Carlos', 40, 'carlos@email.com', '1122-3344')

print(vars(cliente1))
print(vars(cliente2))
print(vars(cliente3))
print('')

print(cliente1)
print(cliente2)
print(cliente3)