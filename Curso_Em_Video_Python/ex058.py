# Ex: 058 - Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em
# um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até
# acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 058
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
sorteado = randint(0, 10)

palpites, acertou = 0, False

while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1

    if jogador == sorteado:
        acertou = True

    else:
        if jogador < sorteado:
            print('Maior... Tente novamente.')

        elif jogador > sorteado:
            print('Menor... Tente novamente.')

print(f'''\nParabéns! Você acertou!
Você teve que tentar {palpites} vezes...''')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
