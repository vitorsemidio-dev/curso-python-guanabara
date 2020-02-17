from math import inf

def fMaior(*num):
    maior = -inf
    for i in range(len(num)):
        if num[i] > maior:
            maior = num[i]
    return maior


maximo = fMaior(1,5,6,15,1,0,0,2)
print(maximo)
