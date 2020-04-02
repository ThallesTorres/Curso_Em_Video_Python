# Ex: 092 - Crie um programa que leia nome, ano de nascimento e carteira de 
# trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS 
# for diferente de ZERO, o dicionário receberá também o ano de contratação 
# e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa 
# vai se aposentar.

from datetime import date

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 092
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

informacoes = dict()

print("--Por favor, preencha o formulário abaixo: ")
informacoes['Nome'] = input("Nome: ").title().strip()
informacoes['Idade'] = date.today().year - int(input("Ano de nascimento: "))
informacoes['Carteira_de_Trabalho_CTPS'] = int(input("Carteira de trabalho [0 caso não tenha]: "))

if informacoes['Carteira_de_Trabalho_CTPS'] != 0:
    informacoes['Ano_Contratacao'] = int(input("Ano de contratação: "))
    informacoes['Salario'] = float(input("Salário: R$"))
    informacoes['Aposentadoria'] = informacoes['Ano_Contratacao'] + 35 - date.today().year + informacoes['Idade']

print("\n--Dados finais")
for chave, valor in informacoes.items():
    print(f"{chave} = {valor}")

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
