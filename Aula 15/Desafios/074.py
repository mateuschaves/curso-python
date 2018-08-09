"""
    Crie um programa que vai gerar cinco números aleatórios e
    colocar em uma tupla.

    Depois disso, mostre a listagem de números gerados e também
    indique o menor e o maior valor que estao na tupla.

    Se for preciso, eu giro a terra inteira
    Até que o tempo se esqueça de ir pra frente e volte atrás
    Milhões de anos, quando todos continentes se encontravam
    Pra que eu possa caminhar até você

    Partilhar - Rubel ♪♫
"""

from random import randint


tupla = (randint(0, 99999), randint(0, 99999), randint(0, 99999), randint(0, 99999), randint(0, 99999), randint(0, 99999))
print(tupla)
ordem = sorted(tupla)
print(f'Maior valor: {ordem[-1]}')
print(f'Menor valor valor: {ordem[0]}')
