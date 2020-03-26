# Ex: 018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor 
# do seno, cosseno e tangente desse ângulo.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 018
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

from math import radians, sin, cos, tan
a = float(input('Digite o ângulo que você deseja: '))
r = radians(a)
seno = sin(r)
print(f'O ângulo de {a} tem o SENO de {seno:.2f}')
coseno = cos(r)
print(f'O ângulo de {a} tem o COSENO de {coseno:.2f}')
tangente = tan(r)
print(f'O ângulo de {a} tem o TANGENTE de {tangente:.2f}')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
