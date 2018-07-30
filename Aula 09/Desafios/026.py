# Faça um programa que leia uma frase
# pelo teclado e mostre

# Quantas vezes aparece a letra A
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece pela última vez

frase = input("Digite uma frase: ")

print("A letra A aparece {} vezes !".format(frase.count('A')))
print("A letra A aparece pela primeira vez em {} !".format(frase.find('A')))
print("A letra A aparece pela última vez em {} !".format(frase.rfind('A')))
