# Um professor quer sortear um dos seus quatro alunos
# para apagar o quadro. Faça um programa que ajue ele,
# lendo o nome deles e escrevendo o nome do escolhido.

import random

a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o nome do segundo aluno: ')
c = input('Digite o nome do terceiro aluno: ')
d = input('Digite o nome do quarto aluno: ')
lista = [a, b, c ,d]
escolhido = random.randint(0, 3)
print('O aluno escolhido foi: {}'.format(lista[escolhido]))
