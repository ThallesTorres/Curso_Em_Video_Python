# Ex: 079 - Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 079
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

print('--Preencha os Dados')

decisao = 's'
valores_unicos = []

while decisao == 's':
    valor = int(input('Digite um valor: '))

    if valor not in valores_unicos:
        valores_unicos.append(valor)
        print('Valor adicionado com sucesso...')

    else:
        print('Falha ao adicionar, número já existente...')

    decisao = ' '
    while decisao not in 'sn':
        decisao = str(input('\nDeseja adicionar outro valor? [S/N] ')).lower()

valores_unicos.sort()
print(f'\nValores digitados: {valores_unicos}')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
