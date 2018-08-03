"""
    Crie um programa que leia um número
    inteiro e mostre na tela se ele é
    PAR ou ÍMPAR.

    If I was young, I'd flee this town
    I'd bury my dreams underground
    As did I, we drink to die, we drink tonight

    Elephant Gun - Beirut ♪♫

"""

n = int(input('Digite um número: '))
if n % 2 == 0:
    print('{} é par !'.format(n))
else:
    print('{} é ímpar !'.format(n))
