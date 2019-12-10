# Ex: 040 - Crie um programa que leia duas notas de um aluno e calcule sua
# média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5 - Reprovado, Média entre 5 e 6.9 - Recuperação,
# Média 7 ou superior - Aprovado.

print('-=-' * 10)
print('--Seja Bem Vindo'
      '\n--Exercício 40')
print('-=-' * 10, '\n')

print('--Preencha os Dados ')
n1 = float(input('1° Nota: '))
n2 = float(input('2° Nota: '))
media = (n1 + n2) / 2
print(f'\nA média entre {n1:.1f} e {n2:.1f} é: {media:.1f}')

if media < 5:
    print('O aluno está Reprovado!')

elif media >= 7:
    print('O aluno está Aprovado! ')

else:
    print('O aluno está em Recuperação! ')

print('')
print('-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles')
print('-=-' * 10, '\n')
