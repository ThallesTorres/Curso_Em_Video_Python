# Ex: 107 - Crie um módulo chamado moeda.py que tenha as funções incorporadas 
# aumentar(), diminuir(), dobra() e metade(). Faça também um programa que 
# importe esse módulo e use algumas dessas funções.

import moeda as m


print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 107
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

m.escreva("Análise de preço")

preco = float(input("Digite o preço: R$"))

print(f"""\n--Análise final
Metade de {preco}: {m.metade(preco)}
Dobro de {preco}: {m.dobro(preco)}
Aumentado em 15%: {m.aumentar(preco, 15)}
Diminuido em 12%: {m.diminuir(preco, 12)}""")

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
