# Ex: 057 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os
# valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter
# um valor correto.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 057
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

print('--Verificador de Sexo\n'
      '--Preencha os Dados')

sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]

while sexo not in 'MF':
    print('Sexo Inválido. Digite novamente...')
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]

print(f'\nSexo {sexo} registrado com sucesso!')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
