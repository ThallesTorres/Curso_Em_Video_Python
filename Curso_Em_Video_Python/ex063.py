# Ex: 063 - Faça um programa que leia um número qualquer e mostre o seu fatorial.
# (ex: 5! = 5x4x3x2x1 = 120)

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 063
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

termo = int(input('Quantidade de termos: '))

valor1, valor2, cont = 0, 1, 3

print('\n--Resultados')
print(f'{valor1} => {valor2}', end='')

while cont <= termo:
    resultado = valor1 + valor2
    print(f' => {resultado}', end='')
    valor1 = valor2
    valor2 = resultado
    cont = cont + 1

print('\n--Fim da Sequência')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
