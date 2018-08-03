"""
    Faça um programa que leia
    um ano qualquer e mostre
    se ele é bissexto.


    Linda
    Do jeito que é
    Da cabeça ao pé

    Do jeitinho que for
    É, e só de pensar
    Sei que já vou estar
    Morrendo de amor
    De amor

    Coisa Linda - Tiago Iorc ♪♫
"""

ano = int(input('Informe o ano: '))

if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print('O ano {} é bissexto !'.format(ano))
else:
    print('O ano {} não é bissexto !'.format(ano))

