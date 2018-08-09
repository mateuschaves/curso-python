"""
    Crie uma tupla preenchida com os 20 primeiros colocados
    da Tabela do Campeonato Brasileiro de Futebol, na ordem
    de colocação. Depois mostre:

    A) Apenas os 5 primeiros colocados.

    B) Os últimos 4 colocados da tabela.

    C) Uma lista com os times em ordem alfabética.

    D) Em que posição na tabela está o time da Chapecoense.

    Havia uma sacola com uma mascara
    E uma garota a encontrou
    De início teve medo
    Não sabia o que fazer
    E nem como compor
    Mas colocou sobre o seu rosto
    E lhe caiu tão bem
    Ficou

    Mascarados - Rubel ♪♫
"""

tabela = ('São Paulo', 'Flamengo', 'Internacional', 'Grêmio', 'Atlético', 'Palmeiras', 'Corinthians', 'Cruzeiro', 'Fluminense', 'América-MG', 'Botafogo', 'Sport Recife', 'Vasco da Gama', 'EC Vitória', 'Santos', 'Bahia', 'Chapecoense', 'Ceará SC', 'Atlético PR', 'Paraná')
ordem = sorted(tabela)
chape = tabela.index('Chapecoense') + 1
print(f'Os primeiros 5 colocados: {tabela[:5]}')
print(f'Os últimos 4 colocados: {tabela[16:]}')
print(f'Os times em ordem alfabética: {ordem}')
print(f'Posíção da Chapecoense: {chape}')
