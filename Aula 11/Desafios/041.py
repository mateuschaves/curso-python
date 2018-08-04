"""
    A confederação nacional de natação precisa de um programa que
    leia o ano de nascimento de um atleta e mostro sua categoria:
    idade =< 9 = mirim
    9 < idade <= 14 = infantil
    14 < idade <= 19 = junior
    19 < idade <= 25 = sênior
    idade > 25 = MASTER

    Não sou nem quero ser o seu dono
    É que um carinho, às vezes, cai bem
    Eu tenho meus desejos e planos secretos,
    Só abro pra você mais ninguém
    Por que você me esquece e some?
    E se eu me interessar por alguém?

    Sozinho - Caetano Veloso ♪♫
"""
from datetime import datetime

nascimento = int(input('Digite seu ano de nascimento: '))
idade = datetime.now().year - nascimento
print('Idade: {}'.format(idade))
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Sênio')
else:
    print('Master')

