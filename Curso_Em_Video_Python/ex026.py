# Ex: 026 - Faça um programa que leia uma frase pelo teclado e mostra: Quantas 
# vezes aparece a letra "A"; Em que posição ela aparece a primeira vez; Em que 
# posição ela aparece a última vez.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 026
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

f = input('Digite uma frase: ').lower().strip()
print(f'A letra "A" aparece {f.count("a")} vezes na frase.')
print(f'A primeira letra "A" apareceu na posição {f.find("a") + 1}')
print(f'A última letra "A" apareceu na posição {f.rfind("a") + 1}')
# Aqui o '+1' é só para o usuário ter uma visão melhor, pois o sistema começa a contagem do 0.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
