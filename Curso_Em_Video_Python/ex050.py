# Ex: 050 - Desenvolva um programa que leia seis números inteiros e mostre
# a soma apenas daqueles que forem pares. Se o valor for ímpar, desconsidere-o.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 050
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

soma = 0
cont = 0

for c in range(0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        soma += n
        cont += 1

print(f'\nVocê informou {cont} números pares.\n'
      f'Soma dos números pares = {soma}')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
