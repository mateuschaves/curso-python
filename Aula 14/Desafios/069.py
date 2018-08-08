"""
    Crie um programa que leia a idade e o sexo de várias pessoas.
    A cada pessoa cadastrada, o programa deverá perguntar se o
    usuário quer ou não continuar. No final, mostre:

    A) Quantas pessoas tem mais de 18 anos.

    B) Quantos homens foram cadastrados.

    C) Quantas mulheres tem menos de 20 anos.

    I fall asleep in my own tears
    I cry for the world, for everyone
    And I build a boat to float in
    I'm floating away

    Warrior - Aurora ♪♫

"""
homens = 0
# Mulheres com menos de 20 anos.
mulheres = 0
# Pessoas com mais de 18 anos.
pessoas = 0

while True:
    idade = int(input('Digite sua idade: '))
    sexo = input('Informe o seu sexo: [H/F/O]').strip()
    if sexo.upper() == 'H':
        homens += 1
    elif sexo.upper() == 'F' and idade < 20:
        mulheres += 1
    if idade > 18:
        pessoas += 1
    resposta = input('Deseja continuar ? [S/N] ')
    if resposta.upper() == 'N':
        break

print(f'{homens} homens cadastrados.')
print(f'{mulheres} mulheres com menos de 20 anos cadastradas.')
print(f'{pessoas} pessoas com mais de 18 anos cadastradas.')
