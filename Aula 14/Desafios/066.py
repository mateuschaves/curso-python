"""
    Crie um programa que leia vários números inteiros pelo teclado.
    O programa só vai parar quando o usuário digitar o valor 999,
    que é a condição de parada. No final, mostre quantos números
    foram digitados e qual foi a soma entre eles (Desconsiderando
    a flag).

    Não se arrisque em tentar
    Me escrever nas suas melhores linhas
    Eu não preciso de altar
    Só vem repousa sua paz na minha
    Eu já te disse alguma vez
    Tu tem pra mim o nome mais bonito.

    Calendário - Anavitória ♪♫
"""

soma = 0
i = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    i += 1
    soma += n
print(f'Foram digitados {i} números !')
print(f'O somatório entre eles é e {soma} !')
