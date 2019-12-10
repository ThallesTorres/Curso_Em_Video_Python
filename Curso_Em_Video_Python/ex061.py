# Ex: 061 - Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('-=-' * 10)
print('--Seja Bem Vindo'
      '\n--Exercício 61')
print('-=-' * 10, '\n')

print('--Progressão Aritmética\n'
      '--Preencha os Dados')
termo = int(input('Número Inicial: '))
razao = int(input('Razão: '))
print('')

cont = 0

while cont < 10:
    print(termo, end=', ')
    termo += razao
    cont += 1

print('Fim\n')
print('-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles Torres')
print('-=-' * 10, '\n')