"""
    Já que você não está aqui
    O que posso fazer é cuidar de mim
    Quero ser feliz ao menos
    Lembra que o plano era ficarmos bem?

    Vento no Litoral - Legião Urbana ♪♫
"""
nome = input('Qual é o seu nome ? ')
if nome.upper() == 'MATEUS':
    print('Que nome bosta !')
elif nome.upper() == 'PEDRO' or nome.upper() == 'MARIA' or nome.upper() == 'PAULO':
    print('Seu nome é bem popular !')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino !')
else:
    print('Nome topperson !')

