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

