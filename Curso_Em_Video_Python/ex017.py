# Ex: 016 - Faça um programa que leia o comprimento do cateto oposto e do cateto 
# adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 017
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenusa vai medir: {hip:.2f}')

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print(f'A hipotenusa vai medir: {hip:.2f}')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
