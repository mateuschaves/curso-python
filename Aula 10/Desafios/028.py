# Escreva um programa que faça o computador
# Pensar um número inteiro entre 0 e 5 e peça
# para o usuário tentar descobrir qual foi o
# número escolhido pelo computador.


"""
    And so Sally can wait
    She knows its too late as we're walking on by
    Her soul slides away
    "But don't look back in anger" I heard you say

    Don't Look Back In Anger - Oasis ♪♫
"""

import random

s = random.randint(0, 5)
n = int(input('Qual o número que eu pensei ? '))

if s == n:
    print('Você acertou, Parabéns !')
else:
    print('Eita, tá errado .-. !')
