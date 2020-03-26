# Ex: 027 - Faça um programa que leia o nome completo de uma pessoa mostrando em 
# seguida o primeiro e o último nome separadamente.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 027
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

n = input('Digite seu nome completo: ').split()
print('Prazer em te conhecer!')
print(f'Seu primeiro nome é {n[0]}')
print(f'Seu último nome é {n[len(n) - 1]}')
# O 'len' começa a contagem no 1, por isso o '-1' (tabela começa pelo 0)

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
