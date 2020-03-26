# Ex: 046 - Faça um programa que mostre na tela uma contagem regressiva para o
# estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1segundo
# entre eles.

from time import sleep
import emoji

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 046
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

for contagem in range(10, 0, -1):
    sleep(1)
    print(contagem)

print(emoji.emojize(':boom:' * 15, use_aliases=True))

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
