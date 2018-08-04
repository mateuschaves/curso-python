"""
    Crie um programa que faça o
    computador jogar Jokenpô com você.


    Não me deixe só
    Eu tenho medo do escuro
    Eu tenho medo do inseguro

    Dos fantasmas da minha voz

    Não Me Deixe Só - Vanessa da Mata ♪♫
"""

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input('Qual é a sua jogada ?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!')

print('-='*11)
print('Jogador jogou {}'.format(itens[jogada]))
print('Computador jogou {}'.format(itens[computador]))
print('-='*11)
if jogada == computador:
    print('O jogo empatou !')
elif jogada == 0 and computador == 1 or computador == 2 and jogada == 1 or computador == 0 and jogada == 2:
    print('O computador ganhou !')
else:
    print('O jogador ganhou !')
