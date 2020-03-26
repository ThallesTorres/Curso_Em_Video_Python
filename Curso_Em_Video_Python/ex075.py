# Ex: 075 - Desenvolva um programa que leia quatro valores pelo teclado e
# guarde-os em uma tupla. No final, mostre: Quantas vezes apareceu o valor 9;
# Em que posição foi digitado o primeiro valor 3; Quais foram os números pares.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 075
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

valores = (int(input('Digite o 1° valor: ')),
           int(input('Digite o 2° valor: ')),
           int(input('Digite o 3° valor: ')),
           int(input('Digite o 4° valor: ')))

cont = 0
for v in valores:
    if v % 2 == 0:
        cont += 1

if 3 in valores:
    x = f'O valor 3 apareceu pela 1ª vez na {valores.index(3) + 1} posição.'
else:
    x = 'O valor 3 não foi digitado nenhuma vez.'

print(f'\n--Dados Finais '
      f'\nValores digitados: {valores} '
      f'\nO valor 9 apareceu {valores.count(9)} vezes. '
      f'\n{x}'
      f'\nFoi digitado {cont} valores pares.')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
