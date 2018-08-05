"""
    Faça um programa que mostre na tela
    uma contagem regressiva para o es-
    touro de fogos de artifício, indo
    de 10 até 0, com uma pausa de 1
    segundo entre eles.

    I went too far when I was begging on my knees
    Begging for your arms, for you to hold them around me
    I went too far and kissed the ground beneath your feet

    Waiting for your love, waiting for our eyes to meet

    I Went Too Far - Aurora ♪♫
"""

from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)
