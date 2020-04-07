# Ex: 099 - Faça um programa que tenha uma função chamada maior(), que receba 
# vários parãmetros com valores inteiros. Seu programa tem que analisar todos 
# os valores e dizer qual deles é o maior.

from time import sleep


def maior(* valores):        
    if len(valores) > 1:
        maior = valores[0]
        
        for num in valores:
            if num > maior:
                maior = num
    
    elif len(valores) == 1:
        maior = valores[0]
        
    else: 
        maior = 0
        
    
    print("--Dados finais:")
    sleep(1)
    print(f"Números fornecidos: {valores}")
    sleep(1)
    print(f"Valores ao todo: {len(valores)}")
    sleep(1)
    print(f"Maior valor: {maior}\n")
    sleep(2)


print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 099
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
