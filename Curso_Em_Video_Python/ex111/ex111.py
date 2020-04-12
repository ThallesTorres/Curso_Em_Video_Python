# Ex: 111 - Crie um pacote chamado utilidadesCeV que tenha dois módulos 
# internos chamados moeda e dado. Transfira todas as funções utilizadas 
# nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo 
# funcionando.

from utilidadescev import moeda


print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 111
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

moeda.escreva("Análise de preço")

preco = float(input("Digite o preço: R$"))

moeda.resumo(preco, 10, 10)

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
