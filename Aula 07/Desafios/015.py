# Escreva um programa que pergunte a quantidade de KM
# percorridos por um carro alugado e a quantidade de
# dias pelos quais ele foi algado. Calcule o preço
# a pagar, sabendo que o carro custa R$ 60 por dia
# e R$ 0,15 por KM rodado.

dias = int(input('Informe a quantidade de dias: '))
km = float(input('Informe a quantidade de KM rodados: '))
price = (dias * 60) + (0.15 * km)
print('O preço total é de: {:.2f} !'.format(price))
