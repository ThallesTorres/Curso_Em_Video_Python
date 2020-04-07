# Ex: 100 - Faça um programa que tenha uma lista chamada números e duas 
# funções chamadas sorteia() e somaPar(). A primeira função vai sortear 
# 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar 
# a soma entre todos os valores PARES sorteados pela função anterior.

def sorteia():
    from random import randint
    
    
    numeros = [randint(0, 9) for x in range(0, 5)]
    
    print("--Valores sorteados:", numeros)
    return numeros
    
    
def somaPar(numeros):
    soma = 0
    
    print("Números pares: ", end='')
    for num in numeros:
        if num % 2 == 0:
            print(num, end=' ')
            soma += num
            
    print(f"\nSoma dos pares: {soma}")
    


print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 100
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

somaPar(sorteia())

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
