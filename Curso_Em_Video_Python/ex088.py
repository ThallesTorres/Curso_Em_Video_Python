# Ex: 088 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números 
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import sample
from time import sleep

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 088
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

jogos = int(input("Total de Jogos a serem sorteados: "))

sorteados = list(sample(range(1, 61), 6) for x in range(jogos))

# for x in range(jogos):
#     sorteados.append(sample(range(1, 61), 6))

print("\n--Números sorteados:")
for cont, jogo in enumerate(sorteados):
    print(f"Jogo {cont + 1}: {sorted(jogo)}")
    sleep(1)

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
