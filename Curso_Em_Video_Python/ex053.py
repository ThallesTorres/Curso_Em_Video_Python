# Ex: 053 - Crie um programa que leia uma frase e diga se ela é um Palíndromo,
# desconsiderando os espaços.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 053
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

print('--Verificador de Frases Palíndromas\n'
      '--Preencha os Dados')
frase_motificada = input('Frase (sem acentuações): ').strip().upper().split()
frase_final = ''.join(frase_motificada)
# inverso = ''

inverso = frase_final[::-1]

# for letra in range(len(frase_final) - 1, -1, -1):
#     inverso += frase_final[letra]

print(f'\nO inverso de {frase_final} é {inverso}')

if inverso != frase_final:
    x = 'NÃO '

else:
    x = ''

print(f'A frase digitada {x}É UM PALÍNDROMO! ')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
