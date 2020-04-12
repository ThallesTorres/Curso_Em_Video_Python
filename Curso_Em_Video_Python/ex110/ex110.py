# Ex: 110 - Adicione ao módulo moeda.py criado nos desafios anteriores, uma 
# função chamada resumo(), que mostre na tela algumas informações que já 
# temos no módulo criado até aqui. 

import moeda


print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 109
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

moeda.escreva("Análise de preço")

preco = float(input("Digite o preço: R$"))

moeda.resumo(preco, 80, 10)

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
