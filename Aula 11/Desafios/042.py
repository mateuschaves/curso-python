"""
    Refaça o desafio 035, acrescentando o recurso de mostrar o tipo de
    triângulo que será formado.

    Eu desço dessa solidão, disparo coisas sobre um chão de giz
    Há meros devaneios tolos a me torturar
    Fotografias recortadas em jornais de folhas amiúde

    Chão de Giz - Oswaldo Montenegro ♪♫
"""

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < b + a:
    print('Os segmentos acima podem formar um triângulo ! ', end='')
    if a == b == c:
        print(' Equilátero !')
    elif a != b != c != a:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Os segmentos acima não podem formar um triângulo !')
