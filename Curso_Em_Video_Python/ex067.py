# Ex: 067 - Faça um programa que mostre a tabuada de vários números, um de cada
# vez, para cada valor digitado pelo usuário. O programa será interrompido
# quando o núemro solicitado for negativo.

print('-=-' * 10)
print('--Seja Bem Vindo'
      '\n--Exercício 67')
print('-=-' * 10, '\n')

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        print('--Programa Finalizado')
        break
    for cont in range(0, 11):
        print(f'{num} x {cont:2} = {num * cont}')

print('')
print('-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles Torres')
print('-=-' * 10, '\n')
