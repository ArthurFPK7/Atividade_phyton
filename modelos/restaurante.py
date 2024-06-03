# criar uma classe Restaurante
class Restaurante:
    nome=''
    categoria=''
    ativo=False

# 2 criação de objetos
restaurante_praca=Restaurante()
restaurante_praca.nome='Praça'
restaurante_praca.categoria='Gourmet'

restaurante_pizza=Restaurante()

restaurantes=[restaurante_praca, restaurante_pizza]

print(dir(restaurante_pizza.ativo))