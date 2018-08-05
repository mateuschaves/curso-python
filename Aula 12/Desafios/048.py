"""
    Faça um programa que calcule a soma
    entre todos os número ímpares que
    são múltiplos de três e que se
    encontram no intervalo de 1 até 500.

    I was dancing in the rain
    I felt alive and I can't complain
    But now take me home
    Take me home where I belong
    I can't take it anymore

    Runaway - Aurora ♪♫

"""
soma = 0
for c in range(0, 500):
    if c % 3 == 0 and c % 2 == 0:
        soma += c
print('A soma dos números múltiplos de 3 entre 1 e 500 é {} !'.format(soma))
