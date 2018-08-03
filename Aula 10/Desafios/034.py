"""
    Escreva um programa que pergunte o salário
    de um funcionário e calcule o valor do seu
    aumento.

    Para salários superiores a R$ 1.250,00
    calcule um aumento de 10%.

    Para salários inferiores ou iguais, o
    aumento é de 15%.

    Come on skinny love, just last the year
    Pour a little salt, we were never here
    My, my, my, my, my, my, my, my

    Staring at the sink of blood and crushed veneer

    Skinny Love - Birdy ♪♫

"""


salario = float(input('Informe o salário do funcionário: '))

if salario > 1250:
    aumento = 0.10 * salario
else:
    aumento = 0.15 * salario

print('O seu novo salário é R$ {:.2f} !'.format(aumento + salario))
