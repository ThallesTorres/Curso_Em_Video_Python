# Ex: 016 - Crie um programa que leia um número Real qualquer pelo teclado e 
# mostre na tela a sua porção Inteira.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 016
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

from math import trunc
n = float(input('Digite um valor: '))
print(f'O valor digitado foi {n} e a sua porção inteira é {trunc(n)}')

'''n = float(input('Digite um valor: '))
print(f'O valor digitado foi {n} e a sua porção inteira é {int(n)}')'''

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
