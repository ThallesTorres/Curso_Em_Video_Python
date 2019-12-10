# Ex: 065 - Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o
# maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
# quer ou não continuar a digitar valores.

print('-=-' * 10)
print('--Seja Bem Vindo'
      '\n--Exercício 65')
print('-=-' * 10, '\n')

print('--Preencha os Dados')

continuar = 's'
media = cont = soma = num = 0
lista = []

while continuar == 's':
    num = int(input('Digite um número: '))
    continuar = input('Quer continuar? [S/N] ').lower().strip()[0]

    lista += [num]
    cont += 1
    soma += num

print(f'''\n--Dados Finais
Números digitados: {cont}
Média: {soma / cont:.2f}
Maior: {max(lista)}
Menor: {min(lista)}''')

print('')
print('-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles Torres')
print('-=-' * 10, '\n')
