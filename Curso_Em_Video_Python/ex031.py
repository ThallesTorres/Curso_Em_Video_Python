# Ex: 031 - Desenvolva um programa que pergunte a destância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km e 
# R$0.45 para viagens mais longas.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 031
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

d = float(input('Digite a distância da viagem em Km: '))
if d <= 200:
    r = d * 0.50
else:
    r = d * 0.45
print(f'Para uma viagem de {d:.1f}Km, custará R${r:.2f}.')
print('Tenha uma boa viagem!')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
