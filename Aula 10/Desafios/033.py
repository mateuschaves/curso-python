"""
    Faça um programa que leia três números
    e mostre qual é o maior e qual é o menor.


    Tudo era tão normal
    Afinal, você vinha me ver
    As tardes passavam

    Mas eu não me lembro
    Como isso acabou

    Me Leve - Plutão Já Foi Planeta ♪♫

"""

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))

if n1 > n2 and n1 > n3:
    if n2 > n3:
        print('{} é o menor !'.format(n3))
    else:
        print('{} é o menor !'.format(n2))
    print('{} é o maior !'.format(n1))
elif n2 > n1 and n2 > n3:
    if n1 > n3:
        print('{} é o menor !'.format(n3))
    else:
        print('{} é o menor !'.format(n1))
    print('{} é o maior !'.format(n2))
else:
    if n1 > n2:
        print('{} é o menor !'.format(n2))
    else:
        print('{} é o menor !'.format(n1))
    print('{} é o maior !'.format(n3))


