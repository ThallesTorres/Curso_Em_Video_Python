# Ex: 090 - Faça um programa que leia nome e média de um aluno, guardando também 
# a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 090
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

aluno = dict()

aluno['Nome'] = input("Nome: ").title()
aluno['Média'] = float(input("Média: "))
aluno['Situação'] = "APROVADO" if aluno['Média'] >= 7 else "Recuperação" if aluno['Média'] >= 5 else "Reprovado"

print("\n--Dados finais")
for y, x in aluno.items():
    print(f"{y}: {x}")

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
