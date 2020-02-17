def escreve(string):
    tam = len(string)
    tam += 2
    linha = "-"*(tam)
    print(linha)
    print(f" {string}")
    print(linha)

string = str(input("Digite sua frase: "))
escreve(string)