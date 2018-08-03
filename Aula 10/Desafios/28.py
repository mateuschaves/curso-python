# Escreva um programa que faça o computador
# Pensar um número inteiro entre 0 e 5 e peça
# para o usuário tentar descobrir qual foi o
# número escolhido pelo computador.

import random

s = random.randint(0, 5)
n = int(input('Qual o número que eu pensei ? '))

if s == n:
    print('Você acertou, Parabéns !')
else:
    print('Eita, tá errado .-. !')
