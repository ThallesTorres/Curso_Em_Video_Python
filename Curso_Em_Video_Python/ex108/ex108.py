# Ex: 108 - Adapte o código do desafio 107, criando uma função adicional 
# chamada moeda() que consiga mostrar os valores como um valor monetário 
# formatado.

import moeda as m


print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 108
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

m.escreva("Análise de preço")

preco = float(input("Digite o preço: R$"))

print(f"""\n--Análise final
Metade de {m.moeda(preco)}: {m.moeda(m.metade(preco))}
Dobro de {m.moeda(preco)}: {m.moeda(m.dobro(preco))}
Aumentado em 15%: {m.moeda(m.aumentar(preco, 15))}
Diminuido em 12%: {m.moeda(m.diminuir(preco, 12))}""")

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
