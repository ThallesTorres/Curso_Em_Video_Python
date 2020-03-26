# Ex: 024 - Crie um programa que leia o nome de uma cidade e diga se ela começa 
# ou não com o nome "SANTO".

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 024
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

cidade = input('Em que cidade você nasceu? ').replace('-', ' ').lower().split()
print(f'Sua cidade começa com "Santo"? {cidade[0] == "santo"}')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
