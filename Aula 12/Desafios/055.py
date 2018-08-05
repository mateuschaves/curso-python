"""
    Faça um programa que leia o peso de cinco pessoas.
    No final, mostre qual foi o maior e o menor peso lidos.

    Ah, quase ninguém vê
    Quanto mais o tempo passa
    Mais aumenta a graça em te viver, iêh

    Ah, e sai sem eu dizer
    Tem mais do que te mostro
    Não escondo quanto gosto de você, êh iêh êh

    Amei Te Ver - Tiago Iorc ♪♫

"""

maior = 0
menor = 0
c = 0
for c in range(0, 5):
    peso = float(input('Informe o seu peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
    if c == 0:
        c += 1
        menor = peso
print('O menor peso lido foi {:.2f} !'.format(menor))
print('O maior peso lido foi {:.2f} !'.format(maior))

