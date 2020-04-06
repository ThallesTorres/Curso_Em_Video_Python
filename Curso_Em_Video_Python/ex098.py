# Ex: 098 - Faça um programa que tenha uma função chamada contador(), que 
# receba três parãmentros: início, fim e passo e ralize a contagem. Seu 
# programa tem que realizar trẽs contagens através da função criada: 
# A- De 1 até 10, de 1 em 1; 
# B- De 10 até 0, de 2 em 2; 
# C- Uma contagem personalizada.

from time import sleep

def contador(inicio, fim, passo):  
    if inicio >= fim:
        passo *= -1
        
    for x in range(inicio, fim, passo):
        print(x, end=' ')
        sleep(0.5)
    
    print()


print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 098
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

contador(1, 10, 1)
contador(10, 0, 2)

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
