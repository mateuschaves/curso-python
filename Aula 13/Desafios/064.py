"""
    Crie um programa que leia vários números
    inteiros pelo teclado. O programa só vai
    parar quando o usuário digitar o valor
    9999, que é a condição de parada. No final,
    mostre quantos números foram digitados e
    qual foi a soma entre eles ( desconsiderando
    a floag )

    Eu poderia acordar sem teu olhar de sono
    Sem teu lábio
    Que é dono
    Mas eu não quero
    Eu não quero

    Porque Eu Te Amo - Anavitória ♪♫

"""

n = 0
s = 0
while 1:
    n = int(input('Informe um número: '))
    if n == 999:
        break
    else:
        s += n
print('O somatório é de {} !'.format(s))
