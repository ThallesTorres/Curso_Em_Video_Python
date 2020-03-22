# Ex: 082 - Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e 
# os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das 
# três listas geradas.


print('-=-' * 10)
print('--Seja Bem Vindo'
      '\n--Exercício 82')
print('-=-' * 10, '\n')

lista, lista_par, lista_impar = [], [], []

while True:
      lista.append(int(input('Digite um valor: ')))

      decisao = input('Deseja adicionar outro valor? [S/N] ').lower()
      if decisao == 'n':
            break

for n in lista:
      if n % 2 == 0:
            lista_par.append(n)
      else:
            lista_impar.append(n)

print(f'''\n--Dados Finais:
Números digitados: {lista}
Números pares: {lista_par}
Números ímpares: {lista_impar}''')

print('')
print('-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles Torres')
print('-=-' * 10, '\n')
