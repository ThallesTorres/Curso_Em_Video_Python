# Ex: 038 - Escreva um programa que leia dois números inteiros e compare-os 
# mostrando na tela uma mensagem: O primeiro valor é maior, O segundo valor é 
# maior ou Não existe valor maior, os dois são iguais.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 038
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

print('--Preencha os Dados: ')
n1 = int(input('1° Número: '))
n2 = int(input('2° Número: '))
print('\n--Dados Finais: ')

if n1 > n2:
    print(f'O primeiro valor ({n1}) é maior. \n')

elif n2 > n1:
    print(f'O segundo valor ({n2}) é maior. \n')

else:
    print(f'Não existe valor maior, os dois {n1, n2} são iguais. \n')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
