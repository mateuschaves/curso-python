"""
    Faça um programa que jogue par ou ímpar com o computador.
    O jogo só será interrompido quando o jogador PERDER,
    mostrando o total de vitórias consecutivas que ele conquis-
    tou no final o jogo.

    Já faz um tempo que eu não sabia
    O que era ser de mim
    E todo dia
    Me dividir, fazer luar
    Desconstruir ideia

    O Tempo É Agora - Anavitória ♪♫
"""
from random import randint
vitorias = 0
while True:
    computador = randint(1, 10)
    jogador = int(input('Digite seu número: '))
    tipo = input('Você quer Par ou Ímpar ? [P/I]  ').strip()
    if (computador + jogador) % 2 == 0:
        par_impar = 'Par'
    else:
        par_impar = 'Ímpar'
    if (computador + jogador) % 2 == 0 and tipo.upper() == 'P' or (computador + jogador) % 2 != 0 and tipo.upper() == 'I':
        print(f'Você venceu ! O computador jogou {computador} e você {jogador} ! {jogador + computador} é {par_impar}')
        vitorias += 1
    else:
        print(f'Você perdeu ! O computador jogou {computador} e você {jogador} ! {jogador + computador} é {par_impar}')
        print(f'Você venceu {vitorias} consecutivas !')
        break
