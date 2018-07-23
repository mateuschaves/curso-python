# O mesmo professor do desafio anterior
# quer sorterar a ordem de apresentação
# e trabalhos dos alunos. Faça um programa
# que leia o nome dos quatro alunos e mostre
# a ordem sorteada.

a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o nome do segundo aluno: ')
c = input('Digite o nome do terceiro aluno: ')
d = input('Digite o nome do quarto aluno: ')
lista = [a, b, c ,d]
lista.sort()
print('1. {}'.format(lista[0]))
print('2. {}'.format(lista[1]))
print('3. {}'.format(lista[2]))
print('4. {}'.format(lista[3]))
