# Ex: 081 - Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A - Quantos números foram digitados.
# B - A lista de valores, ordenada de forma decrescente.
# C - Se o valor 5 foi digitado e está ou não na lista.

print('-=-' * 10)
print('--Seja Bem Vindo'
      '\n--Exercício 81')
print('-=-' * 10, '\n')

lista = []

while True:
      lista.append(int(input(f'Digite um número: ')))
      
      decisao = input('Deseja adicionar outro número? [S/N] ').lower()
      if decisao == 'n':
            break
      
lista.sort(reverse=True)

print(f'''\n--Dados Finais
Total de números digitados: {len(lista)}
Ordenados decrescentes: {lista}
O número 5 {'faz' if 5 in lista else 'não faz'} parte dessa lista.''')

print('')
print('-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles Torres')
print('-=-' * 10, '\n')
