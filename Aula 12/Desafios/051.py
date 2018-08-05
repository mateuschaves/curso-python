"""
    Desenvolva um programa que leia o
    primeiro termo e a razão de uma PA.
    No final, mostre os 10 primeiros termos
    dessa progressão.

    Get up on the floor
    Dancin' all night long
    Get up on the floor
    Dancin' till the break of dawn
    Get up on the floor
    Dancin' till the break of dawn
    Get up on the floor
    Dancin'

    Dancin - Aaron Smith ♪♫

"""

r = int(input('Informe a razão da PA: '))
p = int(input('Informe o primeiro termo da PA: '))
for c in range(p, p + (10 * r), r):
    print(c)


