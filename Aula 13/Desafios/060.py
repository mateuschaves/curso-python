"""
    Faça um programa que leia um número qualquer
    e mostre o seu fatorial
"""

n = int(input('Informe um número: '))
s = n
fatorial = 1
while n > 1:
    fatorial *= n
    n -= 1
print('O fatorial de {} é {} !'.format(s, fatorial))
