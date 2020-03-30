# Ex: 085 - Crie um programa onde o usuário possa digitar sete valores numéricos e 
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 085
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

nums = [[], []]

for cont in range(1, 8):
    num = int(input(f"Digite o {cont}º número: "))
    
    nums[0].append(num) if num % 2 == 0 else nums[1].append(num)

print(f'''\n--Dados finais
Números pares: {sorted(nums[0])}
Números ímpares: {sorted(nums[1])}''')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
