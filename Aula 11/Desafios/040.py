"""
    Crie um programa que leia duas notas de um aluno
    e calcule sua méia, mostrando uma mensagem no final.
    m < 5  = reprovado
    5 < m < 6.9 = recuperação
    m >= 7 = aprovado


    É uma índia com colar
    A tarde linda que não quer se pôr
    Dançam as ilhas sobre o mar
    Sua cartilha tem o A de que cor?

    Relicário - Nando Reis ♪♫
"""

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
m = (n1 + n2) / 2
print('Média : {:.2f}'.format(m))
if m < 5:
    print('Reprovado !')
elif m >= 5 and m < 6.9:
    print('Recuperação !')
else:
    print('Aprovado !')
