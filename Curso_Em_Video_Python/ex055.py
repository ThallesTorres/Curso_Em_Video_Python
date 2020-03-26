# Ex: 055 - Faça um programa que leia o peso de cinco pessoas. No final, mostre
# qual foi o maior e menor peso lidos.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 055
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

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

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
