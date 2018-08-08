"""
    Faça um programa que mostre a tabuada de vários números,
    um de cada vez, para cada valor digitado pelo usuário. O
    programa será interrompido quando o número solicitado for
    negativo.

    Fica
    Fica, me queira e queira ficar
    Fica
    Faz o que quiser de mim
    Contanto que não falte tempo pra me amar

    Fica - Anavitório ♪♫
"""

while True:
    n = int(input('Informe o número da tabuada: '))
    if n < 0:
        break
    for c in range(0, 11):
        print(f'{n} x {c} = {c*n}')


