# Crie um programa que leia o nome completo de uma pessoa e mostre

# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo ( sem os espaços )
# Quantas letras tem o primeiro nome

nome = input("Informe o seu nome: ")
print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ', '')))
nome_quebrado = nome.split()
print(len(nome_quebrado[0].lstrip()))
