"""
   Faça um program que leia o ano de nascimento de um jovem
   e informe se ele ainda vai se alistar ao serviço militar,
   se é a hora de se alistar ou se já passou do tempo do
   alistamento.


    Meu coração carnaval
    Faz de tu minha marchinha favorita
    Te convida pra sambar na sintonia
    No meu peito quando tu se aproximar

    Coração Canarval - Anavitória ♪♫
"""
import datetime
sexo = input('Qual o seu sexo ? ').strip()
if sexo.upper() == 'FEMININO':
    print('Alistamento não obrigatório !')
    exit(1)
nascimento = int(input('Informe o seu ano de nascimento: '))
atual = datetime.datetime.now().year
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
if idade == 18:
    print('É hora de se alistar meu caro !')
elif idade < 18:
    print('Ainda faltam {} anos para o alistamento !'.format(18 - idade))
    print('Seu alistamento será em {}'.format(nascimento + 18))
else:
    print('Passaram {} anos para o alistamento !'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(nascimento + 18))
