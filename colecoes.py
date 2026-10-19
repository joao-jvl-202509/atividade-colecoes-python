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

