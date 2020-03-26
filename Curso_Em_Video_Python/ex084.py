# Ex: 084 - Faça um programa que leia nome e peso de várias pessoas, guardando tudo
# em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas. B) Uma 
# listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 084
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

lista = []
teste = []

continuar = 's'
while continuar == 's':
    
    teste.append(input('Nome: ').title())
    teste.append(int(input('Peso: ')))
    
    lista.append(teste[:])
    teste.clear()
    
    while True:
        continuar = str(input('Deseja adicionar mais? [S/N] ')).lower().strip()[0]
        if continuar in 'sn':
            break

pesado, leve = 0

for x in lista:
    if x == 0:
        pesado = lista[1]
        leve = lista[1]
    else:
        if pesado 

print(f'''--Dados Finais
Pessoas cadastradas: {len(lista)}
Mais pesadas: {pesado}
Mais leves: {leve}''')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
