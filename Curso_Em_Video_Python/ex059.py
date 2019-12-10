# Ex: 059 - Crie um programa que leia dois valores e mostre um menu na tela:
# [1]Somar; [2]Multiplicar; [3]Maior; [4]Novos números; [5] Sair do programa.
# Seu programa deverá realizar a operação solicitada em cada caso.

print('-=-' * 10)
print('--Seja Bem Vindo'
      '\n--Exercício 59')
print('-=-' * 10, '\n')

print('--Preencha os Dados')

n1 = float(input('1° Valor: '))
n2 = float(input('2° Valor: '))

opcao = 0

while opcao != 5:
    print('''\nOpções:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa''')
    opcao = int(input('Digite a opção desejada: '))
    print('')

    if opcao > 5 or opcao == 0:
        print('Opção Inválida. Tente novamente...')
        False

    elif opcao == 4:
        print('--Preencha os Dados')

        n1 = float(input('1° Valor: '))
        n2 = float(input('2° Valor: '))
        False

    elif opcao == 3:
        if n1 > n2:
            print(f'O número {n1} é o maior...')

        elif n1 < n2:
            print(f'O número {n2} é o maior...')

        else:
            print(f'Os números {n1} e {n2} são iguais...')

    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f'{n1} x {n2} = {multiplicacao}')

    elif opcao == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')

print('Programa finalizado. Volte sempre!')

print('')
print('-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles Torres')
print('-=-' * 10, '\n')