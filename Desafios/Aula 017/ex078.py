from random import randint

numeros = []
for i in range(5):
    #numeros.append(int(input(f"Numero {i+1}: ")))
    numeros.append(randint(0, 100))

print(numeros)
print(f"O maior valor da lista eh: {max(numeros)}")
print(f"O menor valor da lista eh: {min(numeros)}")