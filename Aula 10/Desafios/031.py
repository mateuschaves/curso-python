"""
    Desenvolva um programa que
    pergunte a distância de uma
    viagem em KM. Calcule o preço
    da passagem, cobrando R$ 0,50
    por km para viagens de até 200km
    e R$ 0,45 para viagens mais longas.


    Now and then I think of when we were together
    Like when you said you felt so happy you could die
    I told myself that you were right for me

    But felt so lonely in your company
    But that was love and it's an ache I still remember

    Somebody That I Used To Know - Pentatonix ♪♫
"""

distancia = float(input('Informe a distância da viagem em KM: '))

if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45

print('A sua viagem de {:.2f}KM vai custar R$ {:.2f}.'.format(distancia, valor))
