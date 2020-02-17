
def indice (procura, onde):
    for pos, item in enumerate(onde):
        if procura == item:
            return pos
    return -1

tabela = ("Palmeiras", "Flamengo", "Internacional", "Gremio", "Sao Paulo", "Atletico-MG",
          "Atletico-PR", "Cruzeiro", "Botafogo", "Santos", "Bahia", "Fluminense", "Corinthians",
          "Chapecoense", "Ceara", "Vasco", "Sport", "America-MG", "Vitoria", "Parana")

#Apenas os cinco primeiros colocados
print(f"{tabela[:5]}")
#Apenas os quatro ultimos
print(f"{tabela[-4:]}")
#Tabela ordenada
print(sorted(tabela))
posicao = indice('Chapecoense', tabela) + 1
print(f"A Chapecoense encontra-se na posicao {posicao}" if posicao > 0 else "Chapecoense nao participou da Serie A nesse campeonato")