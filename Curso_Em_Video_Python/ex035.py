# Ex: 035 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('--Seja Bem Vindo--')
m1 = float(input('Informe a 1° Medida do triângulo: '))
m2 = float(input('Informe a 2° Medida do triângulo: '))
m3 = float(input('Informe a 3° Medida do triângulo: '))
if (m1 + m2) < m3 or (m1 + m3) < m2 or (m2 + m3) < m1:
      print('De acordo com as medidas informadas, É IMPOSSIVEL FORMAR UM TRIÂNGULO.')
else:
      print('De acordo com as medidas informadas, É POSSIVEL FORMAR UM TRIÂNGULO.')
print('--Obrigado Pelo Uso --'
      '\n--Desenvolvido por Thalles.--')
