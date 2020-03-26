# Ex: 080 - Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 080
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

print('--Preencha os Dados')

lista = []

for x in range(0, 5):
    num = int(input(f'Digite o {x + 1}° Valor: '))

    if x == 0 or num > lista[-1]:
        lista.append(num)

    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1

print(f'\nValores digitados em ordem: {lista}')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
