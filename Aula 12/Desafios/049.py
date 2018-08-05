"""
    Refaça o desafio 009, mostrando a tabuada
    de um número que o usuário escolher, só
    que agora utilizando um laço for.

    I was painting a picture
    The picture was a painting of you and
    For a moment I thought you were here
    But then again, it wasn't true
    Ohh...

    Runaway - Aurora ♪♫

"""

n = int(input('Informe o número que deseja a tabuada: '))

for c in range(0, 11):
    print('{} x {} = {}'.format(n, c, n*c))
