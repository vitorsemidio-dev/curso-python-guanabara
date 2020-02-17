from random import randint
def calcularArea(altura, largura):
    return altura * largura


altura = randint(1, 20)
largura = randint(1, 20)
area = calcularArea(altura, largura)

print(f"Um terreno {altura} X {largura} possui {area}m²")