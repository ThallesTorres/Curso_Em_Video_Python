# Ex: 048 - Faça um programa que calcule a soma entre todos os números
# iímpares que são múltiplos de três e que se escontram no intervalo de
# 1 até 500.

print('-=-' * 10)
print('--Seja Bem Vindo'
      '\n--Exercício 48')
print('-=-' * 10, '\n')

cont = 0
soma = 0

for x in range(1, 501, 2):
    if x % 3 == 0:
        soma += x
        cont += 1
        print(x, end=', ')

print('')
print(f'Total de Números: {cont}\n'
      f'Soma final: {soma}')

print('')
print('-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles')
print('-=-' * 10, '\n')
