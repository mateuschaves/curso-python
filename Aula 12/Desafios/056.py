"""
    Desenvolva um programa que leio o nome, idade
    e sexo de 4 pessoas. No final, mostre:

    A média de idade do grupo.

    Qual é o nome do homem mais velho.

    Quantas mulheres têm menos de 20 anos.

    Posso lhe dar mais mil razões pra te querer
    Coisas que eu já nem sei o nome
    Posso compor mais cem canções de amor
    Pra quê?
    Se quando eu canto você some

    Mil Razões - Tiago Iorc ♪♫

"""

menos_de_20_anos = 0
media = 0
nome_homem_mais_velho = ''
homem_mais_velho = 0
for c in range(0, 4):
    nome = input('Informe o seu nome: ')
    idade = int(input('Informe a sua idade: '))
    sexo = input('Informe o seu sexo: ')
    media += idade
    if idade > homem_mais_velho and sexo.upper() == 'MASCULINO':
        nome_homem_mais_velho = nome
        homem_mais_velho = idade
    if idade < 20 and sexo.upper() == 'FEMININO':
        menos_de_20_anos += 1
print('Média de idade do grupo: {:.2f}'.format(media / 4))
print('Nome do homem mais velho: {}'.format(nome_homem_mais_velho))
print('Mulheres com menos de 20 anos: {}'.format(menos_de_20_anos))
