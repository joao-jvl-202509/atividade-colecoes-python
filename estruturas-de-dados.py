print("=== Listas ===")

frutas = ["Maçã", "Banana", "Uva"]
print(f"Lista inicial: {frutas}")

frutaUsuario = input("Digite uma fruta: ")
frutas.append(frutaUsuario)
print(f"Agora, adicionamos a sua fruta á nossa lista: {frutas}")

frutas[1] = "Morango"
print(f"Agora, tiramos a fruta banana da lista e adicionamos uma nova fruta: {frutas}")

frutas.remove("Uva")
print(f"Agora removemos a fruta uva: {frutas}")

print("\n=== Tuplas ===")

print("Agora, vamos mecher com coordenadas: ")
coordenadas = (-26.3044, -48.8487)
print(f"Coordenadas escolhidas: {coordenadas}")

print(f"Longitude: {coordenadas[1]}")
print(f"Latitude: {coordenadas[0]}")

# coordendas [0] = 25.000, não funcionaria, daria TypeError, já que tuplas são imutáveis

print("\n=== Dicionários ===")

produto = {
    "nome": "Teclado",
    "preco": 120.00,
    "estoque": 10
}

print(f"Dicionário inicial: {produto}")

print(f"Nome do produto: {produto["nome"]}")

precoUsuario = float(input("Digite o novo valor do nosso produto: "))
produto["preco"] = precoUsuario

print(f"O novo preço do produto é de {produto["preco"]}")

# Inserindo uma nova chave

produto["marca"] = "Logitech"
print(f"Nova marca: {produto["marca"]}")

# Listando todas as chaves de produto

print("\nDados completos do produto: ")

for chave, valor in produto.items():
    print(f"{chave} : {valor}")