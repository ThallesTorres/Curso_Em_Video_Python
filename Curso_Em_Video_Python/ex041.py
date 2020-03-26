# Ex: 041 - A Confederação Nacional de Natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade: Até 9 anos - MIRIM, Até 14 anos - INFANTIL,
# Até 19 anos - JUNIOR, Até 20 anos - SÊNIOR, Acima - MASTER.

from datetime import date

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 041
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

print('--Confederação Nacional de Natação')
print('--Preencha os Dados ')
ano_nasc = int(input('Ano de Nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print('')

if idade <= 9:
    categoria = 'mirim'

elif idade <= 14:
    categoria = 'infantil'

elif idade <= 19:
    categoria = 'junior'

elif idade <= 20:
    categoria = 'sênior'

else:
    categoria = 'master'

print(f'O atleta tem {idade} anos.')
print(f'Você está na Categoria: {categoria.upper()}.')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
