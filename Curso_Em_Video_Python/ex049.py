# Ex: 049 - Refaça o DESAFIO 009, mostrando a tabuada de um número que o
# usuário escolher, só que agora utilizando um laço for.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 049
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

n = int(input('Digite um número para ver sua tabuada: '))
print('')

for c in range(0, 11):
    print(f'{n} x {c:2} = {n * c}')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
