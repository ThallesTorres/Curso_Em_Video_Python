# Ex: 043 - Desenvova uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5 - Abaixo do Peso, Entre 18.5 e 25 - Peso Ideal,
# 25 até 30 - Sobrepeso, 30 até 40 - Obesidade, Acima de 40 - Obesidade Mórbida.

print('-=-' * 10)
print('--Seja Bem Vindo'
      '\n--Exercício 43')
print('-=-' * 10, '\n')

print('--Calculo IMC')
print('--Preencha os Dados')
peso = float(input('Peso (Kg): '))
altura = float(input('Altura (m): '))
imc = peso / altura ** 2

if imc < 18.5:
      categoria = 'abaixo do peso'

elif imc < 25:
      categoria = 'peso ideal'

elif imc < 30:
      categoria = 'sobrepeso'

elif imc < 40:
      categoria = 'obesidade'

else:
      categoria = 'obesidade mórbida'

print('')
print(f'IMC: {imc:.1f}\n'
      f'Categoria: {categoria.capitalize()}')

print('')
print('-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles')
print('-=-' * 10, '\n')
