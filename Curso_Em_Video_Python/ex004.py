print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 004
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

algo = input('Digite algo: ')
print(f'O tipo primitivo desse valor é: {type(algo)}')
print(f'Só tem espaços? {algo.isspace()}')
print(f'É um número? {algo.isnumeric()}')
print(f'É alfabético? {algo.isalpha()}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'Estão em maiúscula? {algo.isupper()}')
print(f'Estão em minúscula? {algo.islower()}')
print(f'Está capitalizada? {algo.istitle()}')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
