# Crie um programa que leia um número real
# e mostre a sua porção inteira.

from math import trunc

num = float(input('Informe um número: '))
print('A parte inteira de {} é {}.'.format(num, trunc(num)))
