"""
    Faça um programa que leia o sexo de uma
    pessoa, mas só aceite os valores 'M' ou 'F'.
    Caso esteja errado, peça a digitação nova-
    mente até ter um valor correto.

    We found each other
    I helped you out of a broken place
    You gave me comfort
    But falling for you was my mistake

    Call Out My Name - The Weeknd ♪♫

"""


sexo = input('Qual o seu sexo ? ')
while sexo != 'M' and sexo != 'F':
    sexo = input('Informe M ou F: ')
