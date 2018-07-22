# Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto.

price = float(input('Informe o preço do produto: '))

newPrice = price - (price * 0.05)

print('O novo preço do produto é R$ {:.2f}.'.format(newPrice))
