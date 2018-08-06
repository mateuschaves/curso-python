"""
    Melhore o desafio 061, perguntando para
    o usuário se ele quer mostrar mais alguns
    termos. O programa encerra quando ele
    disser que quer mostrar 0 elementos.


    Stand by me
    Nobody knows
    The way it's gonna be
    Stand by me
    Nobody knows
    The way it's gonna be

    Stand By Me - Oasis ♪♫
"""

p1 = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informe a razão da PA: '))
c  = 0
while c < 10:
    print(p1)
    p1 += r
    c += 1
menu = 1
while menu != 0:
    menu = int(input('Mais quantos elementos você quer mostrar ? '))
    if menu == 0:
        exit(1)
    else:
        c = 0
        while c < menu:
            print(p1)
            p1 += r
            c += 1
