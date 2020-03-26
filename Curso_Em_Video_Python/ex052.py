# Ex: 052 - Faça um programa que leia um número inteiro e diga se ele é ou
# não um número primo.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 052
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

print('--Verificador de Números Primos\n'
      '--Preencha os Dados')
num = int(input('Número: '))
print('\n--Dados Finais')

cont = 0

for c in range(1, num + 1):

    if num % c == 0:
        cont += 1
        print(f'-{c}-', end=', ')

    else:
        print(f'{c}', end=', ')

print('Fim')

if cont == 2:
    conclusao = 'É PRIMO'

else:
    conclusao = 'NÃO É PRIMO'

print(f'O número {num} foi divisível {cont} vezes.\n'
      f'Por isso ele {conclusao}!')

'''if num % 2 == 0 or num % 3 == 0:
    print(f'O número {num} não é primo.')

else:
    print(f'O número {num} é primo.')'''

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
