# Ex: 093 - Crie um programa que gerencie o aproveitamento de um jogador de 
# futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo 
# isso será guardado em um dicionário, incluindo o total de gols feitos durante 
# o campeonato.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 093
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

jogador = dict()

print("--Preencha o formulário abaixo: ")
jogador['Nome'] = input("Nome: ").title().strip()
jogador['Partidas'] = int(input("Partidas jogadas: "))

if jogador['Partidas'] > 0:
    gols = list()
    total_gols = 0
    
    for partida in range(0, jogador['Partidas']):
        x = int(input(f"Gols na {partida + 1}ª partida: "))

        gols.append(x)
        
        total_gols += x
    
    jogador['Gols'] = gols
    jogador['Total_Gols'] = total_gols

print(f"\n--Dados finais")
print(f"O jogador {jogador['Nome']} jogou {jogador['Partidas']} partidas.\n")
print(''.join(f'=> Na {cont+1}° partida, fez {gols} gols.\n' for cont, gols in enumerate(jogador['Gols'])))
print(f"Dando um total de {jogador['Total_Gols']} gols.")

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
