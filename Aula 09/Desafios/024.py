# Crie um programa que leia o nome
# de uma cidade e diga se ela começa
# ou não com o nome "SANTO".

frase = input("Digite uma frase: ").split()
one = frase[0]
print('SANTO' in one.upper())

