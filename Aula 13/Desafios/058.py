"""
    Melhore o jogo do desafio 028 onde o computador
    vai pensar um um número entre 0 e 10. Só que agora
    o jogador vai tentar adivinhar até acertar, mos-
    trando no final quantos palpites foram necessários
    para vencer.

    Wise men say only fools rush in
    But I can't help falling in love with you
    Shall I stay?
    Would it be a sin
    If I can't help falling in love with you?

    Can't Help Falling In Love - Elvis Presley ♪♫
"""

from random import randint
flag = 0
c = 0
computador = randint(0, 10)
while flag != 1:
    jogador = int(input('Digite um número: '))
    c += 1
    if jogador == computador:
        flag += 1
print('Você ganhou em {} jogadas !'.format(c))
