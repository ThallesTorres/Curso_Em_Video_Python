# Ex: 055 - Faça um programa que leia o peso de cinco pessoas. No final, mostre
# qual foi o maior e menor peso lidos.

print('-=-' * 10)
print('--Seja Bem Vindo'
      '\n--Exercício 55')
print('-=-' * 10, '\n')

print('--Verificador de Pesos\n'
      '--Preecha os Dados')

maior, menor = 0, 0

for c in range(1, 6):
    peso = float(input(f'Peso (Kg) da {c}° Pessoa: '))

    if c == 1:
        maior = peso
        menor = peso

    else:
        if peso > maior:
            maior = peso

        if peso < menor:
            menor = peso

print(f'''\n--Dados Finais
Maior Peso: {maior}Kg
Menor Peso: {menor}Kg''')

print('')
print('-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles Torres')
print('-=-' * 10, '\n')
