# Ex: 032 - Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 032
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual. '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(f'O ano {ano} é um ano BISSEXTO.')
else:
    print(f'O ano {ano} NÃO é um ano BISSEXTO.')
print('Tenha um bom dia...')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
