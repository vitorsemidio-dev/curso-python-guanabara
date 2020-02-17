jogador = {}


nome = str(input("Digite o nome do jogador: "))
partidas = int(input(f"Informe quantas partidas o {nome} jogo: "))

jogador["Nome"] = nome
jogador["Gols"] = []
total = 0
for i in range(partidas):
    gols = int(input(f"Gols da partida {i+1}: "))
    jogador["Gols"].append(gols)
    total += gols

jogador["Total"] = total

print(jogador)