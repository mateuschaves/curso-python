"""
    Crie um programa que leia vários números inteiros pelo teclado.
    No final da execução, mostre a média entre todos os valores e qual
    foi o maior e o menor valor lido. O programa deve perguntar ao usuário
    se ele quer ou não continuar a digitar valores.

    Mas, ora
    Você partiu antes de mim
    Nem me deixou barco frágil
    Pr'eu me salvar do naufrágio
    Que foi te dar meu coração

    Barquinho de papel - Anavotória ♪♫
"""

menu = 'S'
menor = 0
maior = 0
c = 0
i = 0
somador = 0
while menu.upper() != 'N':
    n = int(input('Digite um número: '))
    somador += n
    if c == 0:
        c += 1
        menor = n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    i += 1
    menu = input('Deseja continuar ? [S/N]: ')
print('Foram digitados {} números e a média é de {:.2f} !'.format(i, somador / i))
print('O maior número digitado foi {}'.format(maior))
print('O menor número digitado foi {}'.format(menor))
