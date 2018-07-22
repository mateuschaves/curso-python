n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
mo = n1 % n2

print('Soma: {}'.format(s))
print('Multiplicação: {}'.format(m))
print('Divisão: {}'.format(d))
print('Divisão inteira: {:.2f}'.format(di))
print('Potência: {}'.format(e))
print('Resto da divisão: {}'.format(mo))
