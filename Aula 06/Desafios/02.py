# Mostrar todas as informações da entrada.

entrada = input('Digite o que você quiser meu bem: ')

print('{} é numérico ?  {}'.format(entrada, entrada.isnumeric()))
print('{} é alfabético ? {}'.format(entrada, entrada.isalpha()))
print('{} é decimal ? {}'.format(entrada, entrada.isdecimal()))
print('{} é maiúsculo ? {}'.format(entrada, entrada.isupper()))
print('{} é minúsculo ? {}'.format(entrada, entrada.islower()))
