# Ex: 025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 025
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

n = input('Qual é seu nome completo? ').lower().split()
print(f'Seu nome tem Silva? {"silva" in n}')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
