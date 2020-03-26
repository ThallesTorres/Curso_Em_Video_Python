# Ex: 064 - Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a
# condição de parada. No final, mostre quantos números foram digitados e
# qual foi a soma entre eles (desconsiderando o flag(999)).

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 064
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

print('--Preencha os Dados')

num, soma, cont = 0, 0, 0

while num != 999:
    num = int(input('Digite um número [999 para parar]: '))

    if num != 999:
        soma += num
        cont += 1

print(f'\nVocê digitou {cont} números e a soma entre eles é de {soma}')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
