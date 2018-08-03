"""
    Escreva um programa que leia a velocidade de um carro

    Se ele ultrapassar 80km/h, mostre uma mensagem dizendo
    que ele foi multado.

    A multa vai custar R$ 7,00 por cada KM acima do limite.


    It's such a shame for us to part
    Nobody said it was easy
    No one ever said it would be this hard

    The Scientist - Coldplay ♪♫
"""

velocidade = float(input('Informe a velocidade do veículo: '))

if velocidade > 80.0:
    multa = (velocidade - 80) * 7
    print('Você foi multado !')
    print('Total a pagar: R$ {:.2f}.'.format(multa))
else:
    print('Segue o baile !')

