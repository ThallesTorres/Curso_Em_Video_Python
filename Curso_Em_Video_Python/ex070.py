# Ex: 070 - Crie um programa que leia o nome e o preço de vários produtos. O
# programa deverá perguntar se o usuário vai continuar. No final, mostre: Qual
# é o total gasto na compra; Quantos produtos custam mais de R$1000; Qual é o
# nome do produto mais barato.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 070
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

print('--Preencha os Dados')

gasto = mais_de_mil = cont = 0
menor = nome_menor = ' '

while True:
    produto = str(input('Nome do Produto: ')).title().strip()
    preco = float(input('Preço do Produto: R$'))
    gasto += preco
    cont += 1

    if preco > 1000:
        mais_de_mil += 1

    if cont == 1 or preco < menor:
        menor = preco
        nome_menor = produto

    desicao = ' '
    while desicao not in 'SN':
        desicao = str(input('Deseja Continuar? [S/N] ')).upper().strip()[0]

    if desicao == 'N':
        break

    print('-' * 30)

print(f'''\n--Dados Finais
Total de Itens:               {cont}
Total Gasto:                  {gasto}
Mais de R$1.000:              {mais_de_mil}
Nome do Produto Mais Barato:  {nome_menor}''')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
