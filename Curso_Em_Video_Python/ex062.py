# Ex: 062 - Melhore o DESAFIO 061, perguntando para o usuário se ele quer
# mostrar mais alguns termos. O programa encerra quando ele disser que quer
# mostrar 0 termos.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 062
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

print('--Progressão Aritmética\n'
      '--Preencha os Dados')
termo = int(input('Número Inicial: '))
razao = int(input('Razão: '))
print('')

cont, total, mais = 0, 0, 10

while mais != 0:
    total += mais

    while cont < total:
        print(termo, end=', ')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
