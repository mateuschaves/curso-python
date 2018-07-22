# Crie um programa que leia quanto dinheiro
# uma pessoa tem na carteira e mostre quantos
# dólares ela pode comprar. Consirede U$$ 1,00 = R$ 3,27

reais = float(input('Quantos R$ você tem ? '))
dolares = reais / 3.27
print('Você pode comprar US$ {:.2f}.'.format(dolares))
