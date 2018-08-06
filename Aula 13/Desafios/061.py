"""
    Refaça o desafio 051, lendo o primeiro
    termo e a razão de uma PA, mostrando os
    10 primeiros termos da progressão usando
    a estrutura while.

    When the night has come
    And the land is dark
    And the moon is the only light we see
    No I won't be afraid
    No I won't be afraid
    Just as long as you stand, stand by me

    Stand By Me - John Lennon ♪♫
"""

p1 = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informe a razão da PA: '))
c  = 0
while c < 10:
    print(p1)
    p1 += r
    c += 1
