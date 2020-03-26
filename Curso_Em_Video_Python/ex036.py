# Ex: 036 - Escreva um progrma para aprovar o empréstimo bancário para a compra 
# de uma casa. O programa vai perguntar o valor da casa, o salário do comprador 
# e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, dabendo 
# que eka não pode exceder 30% do salário ou então o empréstimo será negado.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 036
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

print('-=-Preencha os Dados-=- ')
valor_casa = int(input('Valor da Casa: R$'))
salario = int(input('Salário do Comprador: R$'))
anos = int(input('Em quantos Anos: '))
meses = anos * 12
prestacao = valor_casa / meses
print('-=-Dados Finais-=-')
print(f'Valor da Casa: R${valor_casa} \nAnos: {anos} \nMeses: {meses} \nPrestações: R${prestacao:.2f}')
if prestacao >= salario * 30 / 100:
    print('Empréstimo Não Aprovado!!)')
else:
    print('Empréstimo Aprovado!!')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
