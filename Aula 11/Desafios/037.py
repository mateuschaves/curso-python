"""
    Escreva um programa que leia um número
    inteiro qualquer e peça para o usuário
    escolher qual será a base de conversão:

    1 para binário
    2 para octal
    3 para hexadecimal

    We know full well there's just time
    So is it wrong to dance this line?
    If your heart was full of love

    Could you give it up?

    Not About Angels - Birdy ♪♫
"""

n = int(input('Informe o número para conversão: '))
c = int(input('Selecione:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n>>>> '))

if c == 1:
    print('{} em binário é {} !'.format(n, bin(n)))
elif c == 2:
    print('{} em octal é {} !'.format(n, oct(n)))
elif c == 3:
    print('{} em hexadecimal é {} !'.format(n, hex(n)))
