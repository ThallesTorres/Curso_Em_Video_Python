# Ex: 094 - Crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários 
# em uma lista. No final, mostre: 
# A- Quantas pessoas foram cadastradas; 
# B- A média de idade do grupo; 
# C- Uma lista com todas as mulheres; 
# D- Uma lista com todas as pessoas com idade acima da média.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 094
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

pessoas = list()
total_idade = cont = 0
mulheres = list()

resp = 's'
while resp == 's':
    pessoa = dict()

    print("--Preencha o formulário abaixo: ")
    
    pessoa['Nome'] = input("Nome: ").title().strip()
    
    while True:
        sexo = input("Sexo [F/M]: ").upper().strip()[0]
        if sexo in 'FM':
            pessoa['Sexo'] = sexo
            break
        print("--Sexo Inválido")
        
    pessoa['Idade'] = int(input("Idade: "))

    cont += 1
    total_idade += pessoa['Idade']
    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa['Nome'])
    
    pessoas.append(pessoa.copy())
    del(pessoa)
    
    while True:
        resp = input("\nDeseja adicionar mais uma pessoa? [S/N] ").lower()
        if resp == 's' or resp == 'n':
            print()
            break
        print("--Valor Inválido")

print("--Dados finais")
print(f"Total de pessoas cadastradas: {cont}")
print(f"Idade média: {total_idade / cont:.1f} anos")
print(f"Mulheres: {''.join(f'-{mulher} ' for mulher in mulheres)}")
print("Pessoas com idade acima da média:")
print(''.join(f"-{pessoa['Nome']} com {pessoa['Idade']} anos. \n" 
              for pessoa in pessoas if pessoa['Idade'] >= total_idade / cont))

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
