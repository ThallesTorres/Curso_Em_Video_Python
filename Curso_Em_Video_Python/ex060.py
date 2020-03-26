# Ex: 060 - Faça um programa que leia um número qualquer e mostre o seu fatorial.
# (ex: 5! = 5x4x3x2x1 = 120)

# from math import factorial

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 060
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

print('--Cálculo do Fatorial\n'
      '--Preencha os Dados')
n = int(input('Número: '))
print('')

c, f = n, 1

while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1

print(f'{f}')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
