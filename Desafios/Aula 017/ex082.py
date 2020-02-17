from random import randint
qtd = randint(10,40)
numeros = []
for i in range(qtd):
    numeros.append(randint(0,100))

#par e impar
paridade = [[], []]

for i in range(qtd):
    paridade[numeros[i] % 2].append(numeros[i])

print(f"Lista: {numeros}")
print(f"Pares: {paridade[0]}")
print(f"Impares: {paridade[1]}")