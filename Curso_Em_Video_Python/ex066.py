# Ex: 066 - Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a
# condição de parada. No final, mostre quantos números foram digitados e qual
# foi a soma entre eles (desconsiderando o flag).

print('-=-' * 10)
print('--Seja Bem Vindo'
      '\n--Exercício 66')
print('-=-' * 10, '\n')

print('--Preencha os Dados')

soma, cont = 0, 0

while True:
    num = int(input(f'Digite o {cont + 1}° número [999 para parar]: '))

    if num != 999:
        soma += num
        cont += 1
    else:
        break

print(f'\nVocê digitou {cont} números e a soma entre eles é de {soma}.')


print('')
print('-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles Torres')
print('-=-' * 10, '\n')
