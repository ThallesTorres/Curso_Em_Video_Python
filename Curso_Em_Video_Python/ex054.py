# Ex: 054 - Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas
# já são maiores.

from datetime import date

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 054
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

print('--Verificador de Maioridade\n'
      '--Preencha os Dados:')

menor_idade, maior_idade = 0, 0

for c in range(1, 8):
    ano = int(input(f'Ano de nascimento da {c}° Pessoa: '))
    ano_atual = date.today().year
    idade = ano_atual - ano

    if idade >= 21:
        maior_idade += 1

    else:
        menor_idade += 1

print(f'''\n--Dados Finais
Maiores de idade: {maior_idade}
Menores de idade: {menor_idade}''')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
