i = 0
while i < 5:
    try:
        a = int(input('Numerador: '))
        b = int(input('Denominador: '))
        r = a / b
    except (ValueError, TypeError):
        print('Tivemos um problema com os tipos de dados que vc digitou')
    except ZeroDivisionError:
        print('Nao podemos dividir por zero')
    except KeyboardInterrupt:
        print('O usuario nao informou dados')
    else:
        print(f'O resultado da divisao foi {r:.1f}')
    finally:
        i += 1
        print(f'Volte smp {i}')

# 113
# Reescreva a funcao leiaInt() que fizemos no desafio 104, incluindo agr a posibilidade da digitacao de um numero de tipo invalido.
# Aproveite e crie tbm uma funcao leiaFloat() com a msm funcionalidade

# 114
# Crie um codigo em Python e teste se o site Pudim está acessível pelo PC usado

# 115
# Crie um pequeno sistema modularizado que permina cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter duas opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas