from math import hypot

x = float(input('Informe o valor do cateto adjacente: '))
y = float(input('Informe o valor do cateto oposto: '))

print('O valor da hipotenusa é {:.2f}.'.format(hypot(x, y)))
