# Ex: 068 - Faça um programa que jogue par ou ímpar com o computador. O jogo só
# será interrompido quando o jogador PERDER, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.

from random import randint

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 068
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

vitoria = 0
tipo = ' '

while True:
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]

    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    soma = computador + jogador

    if tipo == 'P' and soma % 2 == 0:
        vitoria += 1
        resultado = 'PAR'
        print(f'O computador jogou {computador} e você {jogador}. Total de {soma} deu {resultado}.')
        print(f'Você Venceu!!')

    elif tipo == 'I' and soma % 2 != 0:
        vitoria += 1
        resultado = 'ÍMPAR'
        print(f'O computador jogou {computador} e você {jogador}. Total de {soma} deu {resultado}.')
        print(f'Você Venceu!!')

    else:
        print(f'GAME OVER! Você venceu {vitoria} vezes.')
        break

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
