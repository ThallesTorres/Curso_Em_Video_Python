# Aula 13
# Exemplo 01
for c in range(0, 6):
    print('Oi')
print('Fim!!')

# Exemplo 02
for c in range(0, 6):
    print(c)
print('Fim!!')

# Exemplo 03
for c in range(1, 7):
    print(c)
print('Fim!!')

# Exemplo 04
for c in range(6, 0, -1):
    print(c)
print('Fim!!')

# Exemplo 05
for c in range(0, 7, 2):
    print(c)
print('Fim!!')

# Exemplo 06
n = int(input('Digite um número: '))
for c in range(0, n + 1):
    print(c)
print('Fim!!')

# Exemplo 07
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f + 1, p):
    print(c)
print('Fim!!')

# Exemplo 08
for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('Fim!!')

# Exemplo 09
s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s = s + n
print(f'A soma dos valores foi {s}.')
print('Fim!!')