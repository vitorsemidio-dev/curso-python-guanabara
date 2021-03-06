# Curso em Vídeo - Python

## Link Playlist

* [Mundo 1 - Fundamentos](https://www.youtube.com/playlist?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6)
* [Mundo 2 - Estruturas de Controle](https://www.youtube.com/playlist?list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye)
* [Mundo 3 - Estruturas Compostas](https://www.youtube.com/playlist?list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH)
* [Desafios](https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-)


## Lista dos desafios do Mundo 1

[005] Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor

[006] Crie um algoritmo que leia um número e mostreu o seu dobro, triplo e raiz quadrada

[007] Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media

[008] Escreva um programa que leia um valor em metros e o exiba convertido em centrimetros e milimetros

[009] Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

[010] Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$1,00 = R$3,27

[011] Faça um programa que leia a largura e a altura que uma parede, em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

[012] faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

[013] Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

[016] Crie um programa que leia um numero real e mostre sua parte inteira

[017] Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

[018] Faça um programa que leia um ângulo qlqr e mostre na tela o valor do seno, cosse e tangente desse angulo

[019] Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajudeo, lendo o nome deles e escrevendo o nome do escolhido.

[020] O msm professor qr sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

[021] Faça um programa que abra e reproduza o áudio de um arquivo mp3

[022] Crie um programa que leia o nome completo de uma pessoa e mostre:

  * O nome com todas as letras maiúsculas
  * O nome com todas minúsculas
  * Quantas letras ao todo (sem considerar os espaços)
  * Quantas letras tem o primeiro nome


[023] Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. Exemplo:
  ```
    ex: 1834
    unidade: 4
    dezena: 3
    centena: 8
    milha: 1
  ```

[024] Crie um programa leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"


[025] Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome


[026] Faça um programa que leia uma frase pelo teclado e mostre:
  * Quantas vezes aparece a letra "a"
  * Em que posição ela aparece a primeira vez
  * Em que posição ela aparece a última vez


[027] Faça um programa que leia o nome completo de uma pessoa, mostrando o primeiro e ultimo nome

  ```
    ex: Ana Maria de Souza
    primeiro = Ana
    ultio = Souza
  ```

[028] Escrava um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

[029] Escreve um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.

[030] Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar

[031] Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens até 200km e R$0,45 para viagens mais longas.

[032] Faça um programa que leia um ano qualquer e mostre se ele é bissexta.

[033] Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

[034] Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salário superiores a R$1250,00 calcule um amento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

[035] Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

> **[EXTRA] Refaça todos os exercícios utilizando cores no terminal**

## Cores no Terminal

### Estrutura

> **\033[estiloTexto:corTexto:corFundo\033[m**

Abaixo estão os valores aceitáveis:

### Estilo do Texto

  ```python
  style = {
    "fecha":"\033[m",
    "none":"\033[0",
    "negrito":"\033[1",
    "italico":"\033[4",
    "invertido":"\033[7",
  }
  ```

### Cor do Texto

  ```python
  text = {
    "fecha":"\033[m",
    "branco":"\033[30m",
    "vermelho":"\033[31m",
    "verde":"\033[32m",
    "amarelo":"\033[33m",
    "azul":"\033[34m",
    "roxo": "\033[35m",
    "ciano": "\033[36m",
    "cinza": "\033[37m",
  }
  ```

### Cor de Fundo do Texto

  ```python
  back = {
    "fecha":"\033[m",
    "branco":"\033[40m",
    "vermelho":"\033[41m",
    "verde":"\033[42m",
    "amarelo":"\033[43m",
    "azul":"\033[44m",
    "roxo": "\033[45m",
    "ciano": "\033[46m",
    "cinza": "\033[47m",
  }

  ```

## Lista dos desafios do Mundo 2

[036] Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele irá pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.


[037] Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

  * 1 para binário
  * 2 para octal
  * 3 para hexadecimal


[038] Escreve um program aque leia dois números inteiros e compare-os, mostrando na tela uma mensagem

  * O primeiro valor eh maior
  * O segundo valor eh maior
  * Nao existe valor maior, os dois são iguais


[039] Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

  * Se ele ainda vai se alistar ao serviço militar.
  * Se é a hora de se alistar.
  * Se já passou do tempo do alistamento
  * Seu programa também deverá mostrar o tempo que falta ou que passou do prazo



[040] Crie um programa que leia duas notas do aluno e calcule a media.

  * maior ou igual a 7 aprovado
  * menor que 5 reprovado
  * caso contrário recuperação


[041] A Confederação Nacional de Natação precisa de um programa que elia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

  * Ateh nove anos mirim
  * athe 14 infantil
  * ateh 19 junior
  * ateh 20 senior
  * acima master


[042] Refaça o desafio 0305 dos triangulos, acrescentado o recurso de mostrar que tipo de triângulo será formado:

  * Equilátero
  * Isósceles
  * Escalenos


[043] Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status

  * abaixo de 18.5: abaixo do peso
  * entre 18.5 e 25: peso ideal
  * entre 25 e 30: sobrepeso
  * entre 30 e 40: obsidade
  * acima de 40: obesidade morbida


[044] Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento

  * A vista dinheiro/cheque -> 10% de desconto
  * A vista no cartao -> 5% de desconto
  * Em ateh 2x no cartao -> preço normal
  * 3x ou mais no cartao -> 20% de juros


[045] Crie um programa que faça o computador jogar Jokenpô com vc


[046] Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio. Indo de 10 ateh 0, com uma pausa de 1 segundo entre elas.

[047] Crie um programa que mostre na tela todos os numeros pares entre 1 e 50

[048] Faça um programa que calcule a soma entre todos os numeros impares que sao multiplos de três entre 1 e 500


[049] Refaça o desafio 009,


[050] Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares

[051] Desenvolva um programa que leia o primeiro termo e a razão de uma Pa. No final mostre os dez primeiros termos dessa progressao

[052] Faça um programa que leia um numero inteiro e diga se ele é ou não primo.

[053] Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplo

  * apos a sopa
  * a sacada da casa
  * a torre da derrota
  * o lobo ama o bolo
  * anotaram a data da maratona


[054] Crie um programa que leia o ano de nascimento de ste pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantos já são maiores. Considere maioridade = 21 anos

[055] Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor dos pesos lidos


[056] Desenvolva um programa que leia o nome, idade e sexo de quatro pessoas. No final do programa, mostre:

  * A media de idade do grupo
  * Qual o nome do homem mais velho.
  * Quantas mulheres tês menos de 20 anos


[057] Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "m" ou "f". Caso esteja errado, peça a digitação novamente até ter um valor correto.

[058] Melhore o jogo do desafio 028 onde o jogador vai pensar em um numero entre 0 e 10 Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

[059] Crie um programa que leia dois valores e mostre um menu na tela:

  * Somar
  * Multiplicar
  * Maior
  * Novos numeros
  * Sair do programa
  * Seu programa deverá realizar a operação solicitada em cada caso.

[060] Faça um programa que calcule o fatorial de um numero

[061] Refaça o Desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os dez primeiros termos da PA usando while

[062] Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais quantos termos. O programa encerra quando ele disser que quer mostrar 0 termos.

[063] Ler n e mostrar os n primeiros termos da Sequencia de Fibonacci.

[064] Crie um progra que leia vários numeros inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desocnsiderando 999)


[065] Crie um programa que leia vários numeros inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

[066] Crie um progra que leia vários numeros inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desocnsiderando 999)

[067] Faça um programa que mostre a tabuada de vários numeroes, um de cada vez, para cada valor digitado O programa será interrompido quando o número solicitado for negativo.

[068] Faça um programa que jogue par ou impar com o PC. O jogo só será interrompido quando o jogador perder, mostrando o total de vitorias consecutivas.

[069] Crie um programa que leia a idade e sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário qr continuar ou não. No final, mostre:

  ```
  a) quantas pessoas têm mais de dezoito anos.
  b) quantos homens focam cadastrados.
  c) quantas mulheres têm menso de 20 anos
  ```


[070] Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:

  ```
  a) qual é o total gasto na compra.
  b) quantos produtos custam mais de mil reais
  c) qual é o nome do produto mais barato.
  ```


[071] Crie um programa que simule o funcionamento de um caixa eletrônico. no início, pergunte ao usuário qual será o valor a ser sacado e o rpgrama vai informar quantas cédulas de cada valor serão entregues. *obs: considere que o caixa possua cédulas de 50 20 10 e 1*.


[072] Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado entre 0 e 20 e mostrá-lo por extenso.


[073] Crie uma  tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

  ```
  a) apenas os 5 primeiros colocados.
  b) os últimos 4 colocados
  c) Uma lista com os times em ordem alfabética.
  d) Em que posição na tabela está o time da Chapecoense.
  ```


[074] Crie um programa que vai gerar cinco numeros aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.


[075] Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

  ```
  a) quantas vezes apareceu o valor nove.
  b) em que posição foi digitado o primeiro valor 3.
  c) quais foram os números pares
  ```


[077] Crie um programa que tenha uma tupla com várias palavras. Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.



[078] Faça um programa que leia cinco valores numericos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


[079] Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já existe lá dentro, ele não será adicionado. No f inal, serão exibidos todos o valores únicos digitados em ordem crescente.


[080] Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.


[081] Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

  ```
  a) quantos números foram digitados.
  b) a lista de valores, ordenada de forma decrescente.
  c) se o valor cinco foi digitado e está ou não na lista.
  ```


[082] Crie um programa que vai ler vários números e colocar em uma lista. Depois disse, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.


[083] Crie um programa onde o usuário digite uma expressão qualquer que usa parênteses. Seu aplicativo deverá analiser se a expressão passada está com os parênteses abertos e fechados na ordem correta.


[084] Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

  ```
  a) quantas pessoas foram cadastradas.
  b) uma listagem com as pessoas mais pesadas.
  c) uma listagem com as pessoas mais leves.
  ```

[085] Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente.

[086] Crie um programa que crie uma matriz de dimensão 3x3 e preencha os valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.


[087] Aprimore o desafio anterior, mostrando no final:

  ```
  a) a soma de todos os valores pares digitados.
  b) a soma dos valores da terceira coluna.
  c) o maior valor da segunda linha.
  ```



[088] Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai fsortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

[089] Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e, permita que o usuário possa mostrar as notas de cada aluno individualmente.

[090] Faça um programa que leia nome e média de um ano, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrturua na tela

[091] Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.


[092] Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

[093] Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.


[094] Crie um programa que leia nome, sexo de idade de várias pessoas Guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:

  ```
  a) quantas pessoas foram cadastradas
  b) a média de idade do grupo
  c) uma lista com todas as mulheres
  d) uma lista com todas as pessoas com idade acima da média
  ```


[096] Faça um program que tenha uma função chamada área(), que recebe as dimensões de um terreno retangular e mostre a área do terreno.


[097] Faça um programa que tenha uma função chamada escreve(), que recebe um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. ex: escrava(olá, mundo) e a saída deve ser:

  ```
  ------------
  olá, mundo
  ------------
  ```



[098] Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo e realiza a contagem. Seu programa tem que realizar três contagens através da função criada:

  ```
  a) de um até dez, de um em um
  b) de dez até zero, de dois em dois
  c) uma contagem personalizada
  ```


[099] Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

[100] Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar(). A primeira função vai sortear cinco números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.


[101] função voto(ano nascimento) return negado ? opcional ? obrigatorio

[102] fatorial (num, show = False). Se o usuário informar o valor do parâmetro **show**, deve mostrar *n * (n-1) * ... * 1 = resultado*. Se ele não informar o valor do parâmetro, mostre apenas o resultado.


[103] fichar (nome, gol). return O jogador nome fez gol gols no campeonato








