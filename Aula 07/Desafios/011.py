# Faça um programa que leia alargura e a altura
# de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessária para pintá-la
# sabendo que cada litro de tinta pinta uma área de 2m²


largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))

area = altura * largura

quantidade_tinta = area / 2

print('Você vai precisar de {}L de tinta.'.format(quantidade_tinta))
