"""
    Escreva um programa para aprovar
    o empréstimo bancário para a compra
    de uma casa. O programa vai perguntar
    o valor da casa, o salário do comprador
    e em quantos anos ele vai pagar.

    Calcule o valor da prestação mensal,
    sabendo que ela não pode exceder 30%
    do salário.

    I'm trying but I keep falling down
    I cry out but nothing comes now
    I'm giving my all and I know peace will come

    I never wanted to need someone

    Helium - Sia ♪♫
"""

valor_casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o salário do comprador: '))
anos = int(input('Quantos anos vai durar o pagamento ? '))

mensalidade = valor_casa / (anos * 12)

if mensalidade > salario * 0.3:
    print('Você não pode financiar essa casa  !')
else:
    print('A mensalidade será de R$ {:.2f}.'.format(mensalidade))
