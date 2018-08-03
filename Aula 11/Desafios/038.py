"""
    Escreva um programa que leia dois
    números inteiros e compare-os,
    mostrando na tela uma mensagem:

    O primeiro valor é maior

    O segudo valor é maior

    Não existe valor maior.


    Hold on I still want you
    Come back I still need you
    Let me take your hand I'll make you right
    I swear to love you all my life
    Hold on I still need you

    Hold On - Chord Overstreet ♪♫
"""

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    print('O primeiro número é maior !')
elif n2 > n1:
    print('O segundo número é maior !')
else:
    print('Os valores são iguais')
