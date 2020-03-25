# Ex: 022 - Crie um programa que leia o nome completo de uma pessoa e mostra: O nome com todas as letras 
# maiúsculas e minúsculas; Quantas letras ao toddo (sem considerar espaços); Quantas letras tem o primeiro 
# nome.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 022
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

n = input('Digite seu nome completo: ').strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {n.upper()}')
print(f'Seu nome em minúsculas é {n.lower()}')
print(f'Seu nome ao todo tem {len(n) - n.count(" ")} letras')
dividido = n.split()
print(f'Seu primeiro nome é {dividido[0]} e ele tem {len(dividido[0])} letras')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
