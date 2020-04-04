# Ex: 095 - 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários 

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 095
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

jogadores = list()

resp = 's'
while resp == 's':
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
        
    jogadores.append(jogador)
    del(jogador)
        
    while True:
        resp = input("\nDeseja adicionar mais um jogador? [S/N] ").lower()
        if resp == 's' or resp == 'n':
            print()
            break
        print("--Valor Inválido")

print(f"--Dados finais \n {'n°':^5}{'Nome':^10}{'Partidas':^10}{'Gols':^10}{'Total':^10}")
for num, v in enumerate(jogadores):
    print(f"{num:^5}{v['Nome']:^10}{v['Partidas']:^10}{v['Gols']}{v['Total_Gols']:^10}")

while True:
    resp = int(input("\nMostrar algum jogador? [999 para sair] "))
    
    if resp == 999:
        break
    
    if resp not in range(0, len(jogadores)):
        print("--Valor Inválido")
    
    else:
        print(f"\nO jogador {jogadores[resp]['Nome']} jogou {jogadores[resp]['Partidas']} partidas.\n")
        print(''.join(f'=> Na {cont+1}° partida, fez {gols} gols.\n' for cont, gols in enumerate(jogadores[resp]['Gols'])))
        print(f"Dando um total de {jogadores[resp]['Total_Gols']} gols.")

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
