# Ex: 056 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: A média de idade do grupo; Qual é o nome do
# homem mais velho; Quantas mulheres têm menos de 20 anos.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 056
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

soma_idade, mais_velho, cont = 0, 0, 0
nome_mais_velho = ''

print('--Preencha os Dados: ')

for c in range(1, 5):
    print(f'--{c}° Pessoa')
    nome = input(f'Nome: ').capitalize().strip()
    idade = int(input(f'Idade: '))
    sexo = input(f'Sexo [M/F]: ').upper().strip()

    soma_idade += idade

    if sexo != 'M' and sexo != 'F':
        print('Sexo Inválido. Tente Novamente...')

    elif sexo == 'M' and idade >= mais_velho:
        mais_velho = idade
        nome_mais_velho = nome

    elif sexo == 'F' and idade < 20:
        cont += 1

print(f'''\n--Dados Finais:
A Média de Idade do grupo é de {soma_idade / 4:.1f} anos.
O nome do Homem mais velho {nome_mais_velho} e ele tem {mais_velho} anos.
No grupo tem {cont} Mulheres com menos de 20 anos.''')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
