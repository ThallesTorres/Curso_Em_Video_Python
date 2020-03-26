# Ex: 023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada 
# um dos digitos separados.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 023
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

n = int(input('Informe um número: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'Analisando o número {n}')
print(f'Unidade: {u} \nDezena: {d} \nCentena: {c} \nMilhar: {m}')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
