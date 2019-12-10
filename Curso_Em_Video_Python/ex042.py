# Ex: 042 - Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de
# mostrar que tipo de triângulo será formado: Equilátero - Todos os lados
# iguais, Isósceles - Dois lados iguais, Escaleno - Todos os lados diferentes.

print('-=-' * 10)
print('--Seja Bem Vindo'
      '\n--Exercício 42')
print('-=-' * 10, '\n')

print('--Preencha os Dados ')
m1 = float(input('1° Medida do triângulo: '))
m2 = float(input('2° Medida do triângulo: '))
m3 = float(input('3° Medida do triângulo: '))
print('')

if m1 == m2 == m3:
    n = 'EQUILÁTERO'
    print(f'De acordo com as medidas informadas, seu triângulo é {n}')

elif (m1 + m2) <= m3 or (m1 + m3) <= m2 or (m2 + m3) <= m1:
    print('De acordo com as medidas informadas, é impossivel formar um triângulo.')

elif m1 == m2 or m1 == m3 or m2 == m3:
    n = 'ISÓSCELES'
    print(f'De acordo com as medidas informadas, seu triângulo é {n}')

else:
    n = 'ESCALENO'
    print(f'De acordo com as medidas informadas, seu triângulo é {n}')

print('')
print('-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles')
print('-=-' * 10, '\n')
