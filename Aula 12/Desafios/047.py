"""
    Crie um programa que mostre na tela
    todos os números pares que estão
    no intervalo entre 1 e 50.


    I would like to leave this city
    This old town don't smell too pretty and
    I can feel the warning signs running around my mind

    And when I leave this island, I book myself into soul asylum
    I can feel the warning signs running around my mind

    Half the World Away - Aurora ♪♫

"""

for c in range(1, 51):
    if(c % 2 == 0):
        print('{} é par !'.format(c))
