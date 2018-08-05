"""
    Crie um programa que leia o ano de nascimento
    de sete pessoas. No final, mostre quantas pessoas
    ainda não atingiram a maioridade e quantas já são
    maiores.

    Lembro que te vi caminhar
    Já havia um brilho no olhar
    E junto com um sorriso seu
    O teu olhar vem de encontro ao meu
    E o meu dia se fez mais feliz
    Mesmo sem você perto de mim
    Mesmo longe de mim

    Me namora - Natiruts ♪♫

"""

from datetime import datetime
maiores = 0
menores = 0
for c in range(0, 7):
    nascimeto = int(input('Informe a seu ano de nascimento: '))
    if datetime.now().year - nascimeto >= 18:
        maiores += 1
    else:
        menores += 1
print('{} pessoas são maiores de idade !'.format(maiores))
print('{} pessoas são menores de idade !'.format(menores))
