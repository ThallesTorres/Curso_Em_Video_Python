# Ex: 091 - Crie um programa onde 4 jogadores joguem um dado e tenham resultados 
# aleatórios. Guarde esses resultados em um dicionário em ordem, sabendo que o 
# vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 091
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

jogadores = dict()

for jogador in range(1, int(input("Total de jogadores: ")) + 1):
    jogadores[f'jogador_{jogador}'] = randint(0, 6)

print("\n--Valores sorteados:")
for k, v in jogadores.items():
    print(f"{k} tirou o número {v}.")
    sleep(0.5)
    
# print("\n--Ranking final")
# for cont, v in enumerate(sorted(jogadores.items(), key=itemgetter(1), reverse=True)):
#     print(f"{cont+1}° lugar - {v[0]} com o número {v[1]}")
#     sleep(0.5)

print("\n--Ranking final")
for cont, v in enumerate(sorted(jogadores.items(), key=lambda item: item[1], reverse=True)):
    print(f"{cont+1}° lugar - {v[0]} com o número {v[1]}")
    sleep(0.5)

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
