n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 9999:
        break
    s += n
print(f'A somma vale {s}')
