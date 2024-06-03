# criar uma classe Restaurante
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

# 2 criação de objetos
restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

print(dir(restaurante_pizza.ativo))

# 1) 
restaurante_praca.categoria = 'Italiana'

# 2) 
nome_restaurante_praca = restaurante_praca.nome

# 3) 
if restaurante_praca.ativo:
    print("O restaurante está ativo.")
else:
    print("O restaurante está inativo.")

# 4) 
categoria_classe = Restaurante.categoria

# 5) 
restaurante_praca.nome = 'Bistrô'

# 6) 
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

# 7) 
if restaurante_pizza.categoria == 'Fast Food':
    print("A categoria da instância restaurante_pizza é 'Fast Food'.")

# 8) 
restaurante_pizza.ativo = True

# 9) 
print(f"Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}")