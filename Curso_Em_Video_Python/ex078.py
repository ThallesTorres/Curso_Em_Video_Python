# Ex: 078 - Faça um programa que leia 5 valores numéricos e guarde-os em uma
# lista. No final, mostre qual foi o maior e o menor valor digitado e as suas
# respectivas posições na lista.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 078
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

print('--Preencha os Dados')

list_valores = []
for cont in range(0, 5):
    list_valores.append(int(input(f'Digite um valor para a posição {cont}: ')))

pos_min, pos_max = [], []
for pos, valor in enumerate(list_valores):
    if valor == min(list_valores):
        pos_min.append(pos)
    if valor == max(list_valores):
        pos_max.append(pos)

print(f'''--Dados Finais
Valores digitados: {list_valores}
Menor valor {min(list_valores)} na posição {pos_min}
Maior valor {max(list_valores)} na posição {pos_max}''')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
