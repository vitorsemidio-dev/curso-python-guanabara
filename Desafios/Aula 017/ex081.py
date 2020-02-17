from random import randint

qtd = randint(5,20)
numeros = []
for i in range(qtd):
    numeros.append(randint(0, 10))

print(f"Foram lidos {qtd} valores")
numeros.sort(reverse=True)
print(f"A lista em ordem decrescente: {numeros}")
if 5 in numeros:
    print(f"O valor 5 aparece na posicao {numeros.index(5) + 1}")
else:
    print(f"O valor 5 nao aparece")