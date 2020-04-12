# Ex: 109 - Modifique as funções que foram criadas no desafio 107 para que 
# elas aceitem um parãmetro a mais, informando se o valor retornado por elas 
# vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda as m


print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 109
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

m.escreva("Análise de preço")

preco = float(input("Digite o preço: R$"))

print(f"""\n--Análise final
Metade de {m.moeda(preco)}: {m.metade(preco, True)}
Dobro de {m.moeda(preco)}: {m.dobro(preco, True)}
Aumentado em 15%: {m.aumentar(preco, 15, True)}
Diminuido em 12%: {m.diminuir(preco, 12, True)}""")

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
