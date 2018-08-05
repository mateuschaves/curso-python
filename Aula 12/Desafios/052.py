"""
    Faça um programa que leia um número inteiro
    e diga se ele é ou não um número primo.

    Você quer brincar na neve?
    Um boneco quer fazer?
    Você podia me ouvir e a porta abrir
    Eu quero só te ver
    Nós éramos amigas de coração
    Mas isso acabou também
    Você quer brincar na neve?
    Não tem que ser com um boneco

    Vai embora, Anna
    Tudo bem

    Você Quer Brincar Na Neve ? - Frozen ♪♫

"""

v = 0
n = int(input('Informe o número que deseja saber se é primo: '))
for c in range(n, 0, -1):
    if n % c == 0:
        v += 1
if v == 2:
    print('O número {} é primo !'.format(n))
else:
    print('O número {} não é primo !'.format(n))
