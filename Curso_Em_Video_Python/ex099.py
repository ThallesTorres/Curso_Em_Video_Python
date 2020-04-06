# Ex: 099 - Faça um programa que tenha uma função chamada maior(), que receba 
# vários parãmetros com valores inteiros. Seu programa tem que analisar todos 
# os valores e dizer qual deles é o maior.

def maior(* valores):
    nums = list()

    for v in valores:
        nums.append(v)
        
    if len(nums) > 1:
        maior = nums[0]
        
        for num in nums:
            if num > maior:
                maior = num
    
    elif len(nums) == 1:
        maior = nums[0]
        
    else: 
        maior = 0
        
    
    print("--Dados finais:")
    print(f"Números fornecidos: {nums}")
    print(f"Valores ao todo: {len(nums)}")
    print(f"Maior valor: {maior}\n")


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
