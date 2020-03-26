# Ex: 030 - Crie um programa que leia um número inteiro e mostre na tela se ele 
# é Par ou ÍMPAR.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 030
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

n = int(input('Digite um número para saber se ele é ÍMPAR ou PAR: '))
r = n % 2
if r == 0:
    i = 'PAR'
else:
    i = 'ÍMPAR'
print(f'O número {n} é {i}...')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
