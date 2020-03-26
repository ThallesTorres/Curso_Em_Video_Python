# Ex: 077- Crie um programa que tenha uma tupla com várias palavras (não usar
# acentos). Despois disso, você deve mostrar, para cada palavra, quais são as
# suas vogais.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 077
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
vogais = ('a', 'e', 'i', 'o', 'u')

for p in palavras:
    print(f'\nA palavra {p.upper()} tem como vogais ', end='- ')

    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' - ')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
