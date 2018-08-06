"""
    Crie um programa que leia dois valores e
    mostre um menu na tela:

    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa

    Seu programa deverá realizar a operação
    solicitada em cada caso.

    Send me your location
    Let's focus on communicating
    'Cause I just need the time and place to come through
    (A chance to come through)
    Send me your location
    Let's ride the vibrations
    I don't need nothing else but you

    Location - Khalid ♪♫

"""
menu = 0
while menu != 5:
    n1 = float(input('Informe o primeiro valor: '))
    n2 = float(input('Informe o segundo valor: '))
    print("Escolha uma opção abaixo:")
    print(" [ 1 ] Somar")
    print(" [ 2 ] Multiplicar")
    print(' [ 3 ] Maior')
    print(' [ 4 ] Novos números')
    print(' [ 5 ] Sair do programa')
    menu = int(input('Insira a sua escolha: '))
    resultado = 0
    if menu == 1:
        resultado = n1 + n2
    elif menu == 2:
        resultado = n1 * n2
    elif menu == 3:
        if n1 > n2:
            resultado = n1
        else:
            resultado = n2
    elif menu == 4:
        n1 = float(input('Informe o primeiro valor: '))
        n2 = float(input('Informe o segundo valor: '))
    else:
        print('Opção informada não existe !')
    if menu != 4:
        print('O resultado da operação é {:.2f}'.format(resultado))
