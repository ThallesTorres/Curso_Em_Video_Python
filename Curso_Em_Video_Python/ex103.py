# Ex: 103 - Faça um programa que tenha uma função chamada ficha(), que receba 
# dois parãmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum 
# dado não tenha sido informado corretamente.

def ficha(nome='<desconhecido>', gols=0):
    print("\n--Ficha final")
    print(f"O jogador {nome} fez {gols} gol(s) na partida.")


print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 103
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

print("--Ficha de jogadores")

nome = input("Nome: ").capitalize().strip()
gols = input("Gols: ").strip()

if not gols.isnumeric():
    gols = 0

if nome.isalpha():
    ficha(nome, gols)

else: 
    ficha(gols=gols)
    

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
