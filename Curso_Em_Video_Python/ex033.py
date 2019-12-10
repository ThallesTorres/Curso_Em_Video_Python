# Ex: 033 - Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.
from builtins import float

n1 = float(input('Digite o 1° número: '))
n2 = float(input('Digite o 2° número: '))
n3 = float(input('Digite o 3° número: '))
print('Calculando qual é o menor e qual é o maior...')
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O menor número digitado foi {menor}')
print(f'O maior número digitado foi {maior}')
