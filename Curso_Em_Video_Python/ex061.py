# Ex: 061 - Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 061
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

print('--Progressão Aritmética\n'
      '--Preencha os Dados')
termo = int(input('Número Inicial: '))
razao = int(input('Razão: '))
print('')

cont = 0

while cont < 10:
    print(termo, end=', ')
    termo += razao
    cont += 1

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
