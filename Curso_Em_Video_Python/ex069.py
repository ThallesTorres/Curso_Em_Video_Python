# Ex: 069 - Crie um programa que leia a idade e o sexo de várias pessoa. A cada
# pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
# continuar. No final, mostra: Quantas pessoas tem mais de 18 anos; Quantos
# homens foram cadastrados; Quantas mulheres tem menos de 20 anos.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 069
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

print('--Preencha os Dados')

cont = maior_de_18 = homens_cadastrados = mulheres_menores_de_20 = 0

while True:
    print('-' * 30)
    idade = int(input(f'Idade da {cont + 1}° pessoa: '))

    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input(f'Sexo da {cont + 1}° pessoa: [F/M] ')).upper().strip()[0]

    cont += 1

    if idade >= 18:
        maior_de_18 += 1

    if sexo == 'M':
        homens_cadastrados += 1

    if sexo == 'F' and idade < 20:
        mulheres_menores_de_20 += 1

    print('-' * 30)
    desicao = ' '
    while desicao not in 'SN':
        desicao = str(input('Deseja adicionar outra pessoa? [S/N] ')).upper().strip()[0]

    if desicao == 'N':
        break

print(f'''\n--Dados Finais
Pessoas Maiores de 18 Anos: {maior_de_18}
Homens Cadastrados: {homens_cadastrados}
Mulheres com Menos de 20 Anos: {mulheres_menores_de_20}''')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
