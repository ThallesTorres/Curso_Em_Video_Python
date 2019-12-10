# Ex: 076 - Crie um programa que tenha uma tupla única com nomes de produtos e
# seus respectivos preços, na sequência. No final, mostre uma listagem de preços,
# organizando os dados em forma tabular.

print('-=-' * 10)
print('--Seja Bem Vindo'
      '\n--Exercício 76')
print('-=-' * 10, '\n')

produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00,
            "Transferidor", 4.20, "Compasso", 9.99, "Mochila", 120.32, "Canetas",
            22.30, "Livro", 34.90)

print('-' * 40)
for p in produtos:
    if p * 0 != 0:
        print(f'{p:.<30}', end='')
    else:
        print(f'R$ {p:>6.2f}')
print('-' * 40)

'''for i in listagem:
    if type(i) is str:
        print(f'{i:.<32}', end='')
    else:
        print(f'R$ {i:>5.2f}')
print('--'*20)'''

print('')
print('-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles Torres')
print('-=-' * 10, '\n')
