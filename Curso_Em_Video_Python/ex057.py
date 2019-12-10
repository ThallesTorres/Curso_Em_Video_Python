# Ex: 057 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os
# valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter
# um valor correto.

print('-=-' * 10)
print('--Seja Bem Vindo'
      '\n--Exercício 57')
print('-=-' * 10, '\n')

print('--Verificador de Sexo\n'
      '--Preencha os Dados')

sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]

while sexo not in 'MF':
    print('Sexo Inválido. Digite novamente...')
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]

print(f'\nSexo {sexo} registrado com sucesso!')

print('')
print('-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles Torres')
print('-=-' * 10, '\n')
