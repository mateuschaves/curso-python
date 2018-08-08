"""
    Crie um programa que simule o funcionamento de um caixa eletrônico.
    No início, pergunte ao usuário qual será o valor a ser sacado e o
    programa vai informar quantas cédulas de cada valor seráo entregues.

    Obs: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.

    Go row the boat to safer grounds
    But don't you know we're stronger now
    My heart still beats and my skin still feels
    My lungs still breathe, my mind still fears

    But we're running out of time, time
    All the echoes in my mind cry

    Running With The Wolves - Aurora ♪♫
"""

valor = int(input('Informe o valor a ser sacado: '))

um = 0
dez = 0
vinte = 0
cinquenta = 0
while True:
    if valor // 1 % 10 != 0:
        um = valor // 1 % 10
    dezena = valor // 10 % 10
    centena = valor // 100 % 10
    milhar = valor // 1000 % 10
    dezena_milhar = valor // 10000 % 10
    centena_milhar = valor // 100000 % 10
    if dezena == 1:
        dez += 1
    if dezena > 1 and dezena < 5:
        if dezena == 4:
            vinte += 2
        elif dezena == 3:
            vinte += 1
            dez += 1
        elif dezena == 2:
            vinte += 1
    if dezena == 5:
        cinquenta += 1
    if dezena < 100:
        if dezena % 2 == 0:
            vinte += dezena // 2
        else:
            cinquenta += 1
            if (dezena - 5) % 2 == 0:
                vinte += (dezena - 5) // 2
    if centena != 0:
        cinquenta += centena * 2
    if milhar != 0:
        cinquenta += (milhar*1000) // 50
    if dezena_milhar != 0:
        cinquenta += (dezena_milhar*10000) // 50
    if centena_milhar != 0:
        cinquenta += (centena_milhar*100000) // 50
    break
print(f'Notas de R$ 1: {um}')
print(f'Notas de R$ 10: {dez}')
print(f'Notas de R$ 20: {vinte}')
print(f'Notas de R$ 50: {cinquenta}')

