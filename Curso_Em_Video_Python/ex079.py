# Ex: 079 - Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.

print('-=-' * 10)
print('--Seja Bem Vindo'
      '\n--Exercício 79')
print('-=-' * 10, '\n')

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

print('')
print('-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles Torres')
print('-=-' * 10, '\n')
