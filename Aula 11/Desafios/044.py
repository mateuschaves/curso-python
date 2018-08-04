"""
    Elabore um programa que calcule o valor a ser pago por um produto,
    considerando o seu preço normal e condição de pagamento:

    À vista dinheiro/cheque: 10% de desconto

    Á vista no cartão: 5% de desconto

    Em até 2x no cartão: preço normal

    3x ou mais no cartão: 20% de juros


    É só isso
    Não tem mais jeito
    Acabou

    Boa sorte
    Não tenho o que dizer
    São só palavras
    E o que eu sinto
    Não mudará

    Boa Sorte - Vanessa da Mata, Ben Harper ♪♫
"""
t = ''
preco = float(input('Informe o preço do produto: '))
print('Escolha a condição de pagamento: ')
print('[ 1 ] À vista dinheiro/cheque, 10% de desconto.')
print('[ 2 ] À vista no cartão, 5% de desconto.')
print('[ 3 ] Em até 2x no cartão, preço normal.')
print('[ 4 ] 3x ou mais no cartão, 20% de juros.')
cp = int(input('Escolha uma opção de pagamento: '))
if cp == 1:
    v = preco * 0.10
    preco -= v
    t = ' desconto '
elif cp == 2:
    v = preco * 0.05
    preco -= v
    t = ' desconto '
elif cp == 3:
    v = 0
    t = 'nada'
elif cp == 4:
    v = preco * 0.20
    preco += v
    t = ' aumento '
print('O valor total a ser pago é de R$ {:.2f}'.format(preco))
if t.strip() != 'nada':
    print('Houve um{}de R$ {}'.format(t, v))
