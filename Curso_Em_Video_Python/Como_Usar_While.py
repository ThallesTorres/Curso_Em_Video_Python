# Aula 14
# Exemplo 01
c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim!!')

# Exemplo 02
n = 1
while n != 0:
    int(input('Digite um valor: '))
print('Fim!!')

# Exemplo 03
r = 's'
while r == 's':
    n = int(input('Digite um número: '))
    r = input('Quer Continuar? [S/N] ').lower()
print('Fim!!')

# Exemplo 04
n = 1
i = 0
p = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            p += 1
        else:
            i += 1
print(f'Você digitou {p} números pares e {i} números ímpares! ')
