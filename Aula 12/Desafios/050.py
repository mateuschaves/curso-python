"""
    Desenvolva um programa que leia seis
    números inteiros e mostre a soma apenas
    daqueles que forem pares. Se o valor
    digitado for ímpar, desconsidere-o.

    Oh, give me some love, give me some love and hold me
    Give me some love and hold me tight
    Oh, give me some love, give me some love and hold me
    Give me some love and hold me tight

    I Went Too Far - Aurora ♪♫

"""
soma = 0
for c in range(0,6):
    n = int(input('Informe um número: '))
    if n % 2 == 0:
        soma += n
print('A soma dos números pares informados é de {}'.format(soma))
