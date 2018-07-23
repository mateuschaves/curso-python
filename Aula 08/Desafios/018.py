# Faça um programa que leia um ângulo
# qualquer e mostre na tela o valor
# do seno, cosseno e tangete desse ângulo.

from math import cos, sin, tan, radians

angulo = float(input('Informe o valor do ângulo: '))
print('Cos({}) = {}'.format(angulo, cos(radians(angulo))))
print('Sin({}) = {}'.format(angulo, sin(radians(angulo))))
print('Tan({}) = {}'.format(angulo, tan(radians(angulo))))
