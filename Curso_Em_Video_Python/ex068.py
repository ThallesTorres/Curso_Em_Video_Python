# Ex: 068 - Faça um programa que jogue par ou ímpar com o computador. O jogo só
# será interrompido quando o jogador PERDER, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.

from random import randint

print('-=-' * 10)
print('--Seja Bem Vindo'
      '\n--Exercício 68')
print('-=-' * 10, '\n')

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

print('')
print('-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles Torres')
print('-=-' * 10, '\n')
