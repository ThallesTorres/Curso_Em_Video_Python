# Ex: 096 - Faça um programa que tenha uma função chamada área(), que receba 
# as dimensões de um terreno retangular(largura e comprimento) e mostre a 
# área do terreno.

def area(a, b):
    print("\n--Dados finais:")
    print(f"Área de um terreno {a}x{b} é de {a * b}m².")
    

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 096
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

print("--Preencha:")
l = float(input("Largura (m): "))
c = float(input("Comprimento (m): "))
area(l, c)

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
