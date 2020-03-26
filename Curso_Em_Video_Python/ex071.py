# Ex: 071 - Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 071
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

print('--Preencha os Dados')
valor = int(input('Valor a ser sacado: R$'))

cinquenta = vinte = dez = um = 0

while valor >= 50:
    valor -= 50
    cinquenta += 1

while valor >= 20:
    valor -= 20
    vinte += 1

while valor >= 10:
    valor -= 10
    dez += 1

while valor >= 1:
    valor -= 1
    um += 1

print(f'\nNotas de R$50: {cinquenta} ' if cinquenta > 0 else '',
      f'\nNotas de R$20: {vinte} ' if vinte > 0 else '',
      f'\nNotas de R$10: {dez} ' if dez > 0 else '',
      f'\nNotas de R$1: {um} ' if um > 0 else '')

'''valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break'''

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
