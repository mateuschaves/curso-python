# Faça um programa que leia o comprimento
# do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calule e
# mostre o comprimento da hipotenusa.

from math import hypot

x = float(input('Informe o valor do cateto adjacente: '))
y = float(input('Informe o valor do cateto oposto: '))

print('O valor da hipotenusa é {:.2f}.'.format(hypot(x, y)))
