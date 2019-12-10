# Ex: 077- Crie um programa que tenha uma tupla com várias palavras (não usar
# acentos). Despois disso, você deve mostrar, para cada palavra, quais são as
# suas vogais.

print('-=-' * 10)
print('--Seja Bem Vindo'
      '\n--Exercício 77')
print('-=-' * 10, '\n')

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
vogais = ('a', 'e', 'i', 'o', 'u')

for p in palavras:
    print(f'\nA palavra {p.upper()} tem como vogais ', end='- ')

    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' - ')

print('')
print('-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles Torres')
print('-=-' * 10, '\n')
