"""
    Escreva um programa que leia um número
    n inteiro qualquer e mostre na tela os
    n primeiros elementos de uma sequência
    de Fibonacci.

    Ai, amor
    Será que tu divide a dor
    Do teu peito cansado
    Com alguém que não vai te sarar?

    Ai, amor - Anavitória ♪♫
"""

n = int(input('Insira o valor de n: '))
c = 2
sequence = [0, 1]
if n > 2:
    while c < n:
        sequence.append( sequence[ c - 1] + sequence[c - 2] )
        c += 1
print(sequence)
