# Ex: 112 - Dentro do pacote utilidadesCeV que criamos no desafio 111, 
# temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() 
# que seja capaz de funcionar como uma validação de dados para aceitar 
# apenas valores que sejam monetários.

from utilidadescev import moeda, dados


print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 112
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

moeda.escreva("Análise de preço")

preco = dados.leiaDinheiro("Digite o preço: R$")

moeda.resumo(preco, 10, 10)

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
