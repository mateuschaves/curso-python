"""
    Crie um programa que leia uma frase
    qualquer e diga se ela é um palíndromo,
    desconsiderando os espaços.

    Yeah, you never said a word
    You didn't send me no letter
    Don't think I could forgive you

    See our world is slowly dying
    I'm not wasting no more time
    Don't think I could believe you

    Prayer in C - Lilly Wood & The Prick ♪♫
    
"""

frase = input('Insira a frase: ')
frase_sem_espaco = frase.replace(' ', '')
for c in range(0, len(frase_sem_espaco)):
    if frase_sem_espaco[c] != frase_sem_espaco[len(frase_sem_espaco) - c - 1]:
        print('Vish, Num é não !')
        exit(0)
print('A frase {} é um políndromo !'.format(frase))
