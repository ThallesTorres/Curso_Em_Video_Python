# Ex: 051 - Desenvolva um programa que leia o primeiro termo e a razão de uma
# PA. No final. mostre os 10 primeiros termos dessa progressão.

print('-=-' * 10)
print('--Seja Bem Vindo'
      '\n--Exercício 51')
print('-=-' * 10, '\n')

print('--Progressão Aritmética\n'
      '--Preencha os Dados')
termo1 = int(input('Número Inicial: '))
razao = int(input('Razão: '))
print(f'\n{termo1}', end=', ')

for c in range(1, 10):
    termo1 = termo1 + razao
    print(termo1, end=', ')

print('Fim!\n')
print('-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles')
print('-=-' * 10, '\n')
