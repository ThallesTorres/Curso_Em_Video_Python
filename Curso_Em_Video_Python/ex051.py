# Ex: 051 - Desenvolva um programa que leia o primeiro termo e a razão de uma
# PA. No final. mostre os 10 primeiros termos dessa progressão.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 051
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

print('--Progressão Aritmética\n'
      '--Preencha os Dados')
termo1 = int(input('Número Inicial: '))
razao = int(input('Razão: '))
print(f'\n{termo1}', end=', ')

for c in range(1, 10):
    termo1 = termo1 + razao
    print(termo1, end=', ')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
