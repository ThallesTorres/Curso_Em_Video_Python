# Ex: 034 - Escreva um programa que pergunte o salário de um funcionário e calcule 
# o valor do seu aumento. Para salários superiores a R$1.250,00, calcule um aumento 
# de 10%. Para os inferiores ou iguais, o aumento é de 15%.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 034
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

salario = float(input('Salário do Funcionário: R$'))
print('-' * 5, 'Dados', '-' * 5)
if salario <= 1250:
    novo_salario = salario + (salario * 15 / 100)
else:
    novo_salario = salario + (salario * 10 / 100)
print(f'Salário Antigo:     R${salario:.2f} '
      f'\nNovo Salário:       R${novo_salario:.2f}')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
