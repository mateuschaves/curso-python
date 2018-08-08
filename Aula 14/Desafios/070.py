"""
    Crie um programa que leia o nome e o preço de vários produtos.
    O programa deverá perguntar se o usuário vai continuar. No final,
    mostre:

    A) Qual é o total gasto na compra.

    B) Quantos produtos custa mais de R$ 1000

    C) Qual é o nome do produto mais barato.


    Well, you only need the light when it's burning low
    Only miss the sun when it starts to snow
    Only know you love her when you let her go
    Only know you've been high when you're feeling low
    Only hate the road when you're missin' home
    Only know you love her when you let her go

    And you let her go

    Let Her Go - Passenger ♪♫
"""
# Total gasto na compra.
total = 0

# Quantidade de produtos que custam mais de R$ 1000.
quantidade = 0

# Nome do produto mais barato.
produto = ''

# Preço do produto mais barato.
menor_preco = 0

c = 0
while True:
    nome = input('Digite o nome do produto: ').strip()
    preco = float(input('Digite o preço do produto: '))
    total += preco

    if c == 0:
        c += 1
        menor_preco = preco

    if preco > 1000:
        quantidade += 1

    if preco < menor_preco:
        menor_preco = preco
        produto = nome
    resposta = input('Deseja continuar ? [S/N]: ').strip()
    if resposta.upper() == 'N':
        break

print(f'Quantidade de produtos que custa mais de R$ 1000: {quantidade}.')
print(f'Nome do produto mais barato: {nome}.')
print(f'Valor total da compra: R$ {total:.2f}.')
