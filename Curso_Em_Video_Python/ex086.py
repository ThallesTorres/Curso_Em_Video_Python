# Ex: 086 - Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores 
# lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 086
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

matriz = [[], [], []]

for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(int(input(f"Valor para [{linha}, {coluna}]: ")))

# # Tentativa falha ao tentar fazer com o 'join', faltou a parte de quebrar a linha...
# print(f"--matriz \n {''.join(f'[{coluna: ^ 5}] ' for linha in range(3) for coluna in matriz[linha])}")

print("\n--matriz")
for linha in range(3):
    for coluna in matriz[linha]:
        print(f"[{coluna: ^ 5}] ", end='')
    print()

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
