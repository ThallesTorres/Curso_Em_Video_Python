# Ex: 074 - Crie um programa que vai gerar cinco números aleatórios e colocar em
# uma tupla. Depois disso, mostre a listagem de números gerados e também indique
# o menor e o maior valor que estão na tupla.

from random import randint

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 074
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

num = (randint(0, 10), randint(0, 10), randint(0, 10),
       randint(0, 10), randint(0, 10))

print('Números sorteados: ', end='- ')

for n in num:
    print(n, end=' - ')

print(f'''\nMenor: {min(num)}
Maior: {max(num)}''')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
