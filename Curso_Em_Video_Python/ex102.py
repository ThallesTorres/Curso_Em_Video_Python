# Ex: 102 - Crie um programa que tenha uma função fatorial() que receba dois 
# parãmetros: o primeiro que indique o número a calcular e o outro chamado 
# show, que será um valor lógico (opcional) indicando se será mostrado ou 
# não na tela o processo de cálculo do fatorial.

def fatorial(num, show=True):
    '''
    => Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: Retorna o valor do Fatorial de um número.
    '''
    
    resultado = 1
    
    for x in range(num, 0, -1):
        resultado *= x
        
        if show:
            if x == 1:
                print(x, end=' = ')
            else:
                print(x, end='.')       
    
    return f'{resultado}'


print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 102
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

print("--Calculo fatorial")
num = int(input("Valor: "))
show = True if input("Deseja mostrar a conta? [S/N] ").lower() == 's' else False

print(fatorial(num, show))

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
