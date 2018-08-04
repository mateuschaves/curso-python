"""
    Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
    calcule seu IMC e mostre seu status.


    Rasgue as minhas cartas
    E não me procure mais
    Assim será melhor, meu bem

    O retrato que eu te dei
    Se ainda tens, não sei
    Mas se tiver, devolva-me

    Devolva-me - Adriana Calcanhotto ♪♫
"""

peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))
imc = peso / altura ** 2
print('Com o IMC de {:.2f} você está '.format(imc), end='')
if imc < 18.5:
    print('abaixo do peso !')
elif imc < 25:
    print('no peso ideal !')
elif imc < 30:
    print('com sobrepeso !')
elif imc < 40:
    print('obeso !')
else:
    print('com obesidade mórbida !')

