"""
    Desenvolva um programa que leia quatro valores
    pelo teclado e guarde-os em uma tupla. No final,
    mostre:

    A) Quantas vezes apareceu o valor 9.

    B) Em que posição foi a digitado o primeiro valor 3.

    C) Quais foram os números pares.

    Mas se você vier
    Prepara a cama e o colchão
    A roupa limpa e o lençol
    Que dá uma vontade de ficar

    Pearl - Rubel ♪♫
"""
from random import randint

tupla = (randint(0,10), randint(0,10), randint(0,10), randint(0,10))
nove = tupla.count(9)
if tupla.count(3) > 0:
    tres = tupla.index(3)
else:
    tres = 0

print(tupla)
print('Números pares da tupla: ', end=' ')
for pos, c in enumerate(tupla):
    if c % 2 == 0 and pos != 3:
        print(f'{c}', end=' ')
    elif c % 2 == 0 and pos == 3:
        print(f'{c}')
    elif pos == 3:
        print('')
print(f'O número 9 apareceu {nove} vezes !')
print(f'O número 3 foi digitado na posição {tres} da tupla !')
