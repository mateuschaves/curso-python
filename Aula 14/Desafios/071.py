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
total = valor
cedula = 50
total_cedulas = [0, 0, 0, 0]
while True:
    if total == 0:
        break
    elif total >= 50:
        total -= 50
        total_cedulas[0] += 1
    elif total >= 20:
        total -= 20
        total_cedulas[1] += 1
    elif total >= 10:
        total -= 10
        total_cedulas[2] += 1
    else:
        total -= 1
        total_cedulas[3] += 1

print(f'Notas de R$ 50: {total_cedulas[0]}')
print(f'Notas de R$ 20: {total_cedulas[1]}')
print(f'Notas de R$ 10: {total_cedulas[2]}')
print(f'Notas de R$ 1: {total_cedulas[3]}')
