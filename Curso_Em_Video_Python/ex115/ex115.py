# Ex: 115 - Crie um pequeno sistema modulorizado que permita cadastrar pessoas 
# pelo seu nome e idade em um arquivo de texto simples. O sistema só vai ter 2 
# opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

def linha():
    print('\033[33m', end='')
    print('-' * 40)
    print('\033[m', end='')
    

def titulo(msg='VAZIO'):
    linha()
    print(f'{msg.upper():^40}')
    linha()
    
    
def printERRO(msg='VAZIO'):
    print(f'\033[31m--{msg}\033[m\n')
    


    
    
def menu():
    titulo('Menu principal')
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair')
    linha()
    
    while True:
        try:
            x = int(input('Opção desejada: '))
            
        except ValueError:
            printERRO('Erro, digite somente números inteiros entre 1 e 3.')

        except Exception as erro:
            printERRO(f'Erro Inesperado.\n{erro.__class__}')
        
        else:
            if x not in range(1, 4):
                printERRO('Erro, digite somente números inteiros entre 1 e 3.')
                
            else:
                print()
                return x
            
    
def ver():
    with open('/home/fatality/Área de Trabalho/MegaNuvem/Projetos_GitHub/Curso_Em_Video_Python/Curso_Em_Video_Python/ex115/dados.txt') as dados:
        for linha in dados:
            print(linha)
            


def cadastrar():
    with open('/home/fatality/Área de Trabalho/MegaNuvem/Projetos_GitHub/Curso_Em_Video_Python/Curso_Em_Video_Python/ex115/dados.txt', 'a') as dados:
        dados.write(input('Nome: '))
    
    
def sair():
    while True:
        try:
            opcao = input('\nRealmente deseja SAIR? [S/N] ').upper().strip()
            
        except Exception as erro:
            printERRO(f'Erro Inesperado.\n{erro}')
            
        else:
            if len(opcao) == 1 and opcao in 'SN':
                # if opcao == 'S':
                #     return False
                # if opcao == 'N':
                #     return True
                return True if opcao == 'N' else False
            
            else:
                printERRO('Erro, digite somente [S/N].')

        
    
    

        


print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 115
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

x = True
while x:   
    opcao = menu()
    
    if opcao == 1:
        ver()
        
    elif opcao == 2:
        cadastrar()
        
    else:
        x = sair()

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
