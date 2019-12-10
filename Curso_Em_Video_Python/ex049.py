# Ex: 049 - Refaça o DESAFIO 009, mostrando a tabuada de um número que o
# usuário escolher, só que agora utilizando um laço for.

print('-=-' * 10)
print('--Seja Bem Vindo'
      '\n--Exercício 49')
print('-=-' * 10, '\n')

n = int(input('Digite um número para ver sua tabuada: '))
print('')

for c in range(0, 11):
    print(f'{n} x {c:2} = {n * c}')

print('')
print('-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles')
print('-=-' * 10, '\n')
