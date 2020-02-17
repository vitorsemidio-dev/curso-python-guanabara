from random import randint

qtd = randint(5, 20)
numeros = []
for i in range(qtd):
    x = randint(0, 20)
    if x in numeros:
        print(f"\033[31mO valor {x} jah existe na lista. Portanto, ele não foi adicionado\033[m")
        continue

    numeros.append(x)
print(f"Foram lidos {qtd} numeros")
print(f"Os valores lidos ordenados: ", end="")
numeros.sort()
for num in numeros:
    print(f"\033[34m{num}", end=" ")
