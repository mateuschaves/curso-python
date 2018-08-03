"""
    Desenvolva um programa que leia
    o comprimento de três retas e
    diga se elas podem ou não formar
    um triângulo.

    'Cause every time you hurt me, the less that I cry
    And every time you leave me, the quicker these tears dry
    And every time you walk out, the less I love you
    Baby, we don't stand a chance, it's sad but it's true
    I'm way too good at goodbyes

    Too Good at Goodbyes - Sam Smith ♪♫
"""

a = int(input('Informe o comprimento da primeira reta: '))
b = int(input('Informe o comprimento da segunda reta: '))
c = int(input('Informe o comprimento da terceira reta: '))

if a < b + c and b < c + a and c < b + a:
    print('As retas {}, {} e {} podem formar um triângulo !'.format(a, b, c))
else:
    print('As retas {}, {} e {} não podem formar um triângulo !'.format(a, b, c))
