# Ex: 072 - Crie um programa que tenha uma tupla totalmente preenchida com uma
# contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por
# extenso.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 072
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete',
            'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
            'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

continuar = 'S'
while continuar == 'S':
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente Novamente.')

    print(f'Você digitou o número -{contagem[num]}-.\n')

    while True:
        continuar = str(input('Deseja Continuar? [S/N] ')).upper().strip()[0]
        if continuar in 'SN':
            print('')
            break

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
