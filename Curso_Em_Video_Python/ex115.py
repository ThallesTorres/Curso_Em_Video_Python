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
    
    
def printRed(msg='VAZIO'):
    print(f'\033[31m{msg}\033[m')
    


    
    
def menu():
    titulo('Menu principal')
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair')
    linha()
    
    while True:
        try:
            opcao = input('Opção desejada: ')

        except Exception as erro:
            printRed(f'--Erro Inesperado.\n{erro}')
        
        else:
            if len(opcao) == 1 and opcao in range(1, 4):
                return opcao
            
            else:
                printRed('--Opção Inválida.\n')
    
    
def sair():
    while True:
        try:
            opcao = input('Realmente deseja SAIR? [S/N] ').upper().strip()
            
        except Exception as erro:
            printRed(f'--Erro Inesperado.\n{erro}')
            
        else:
            if len(opcao) == 1 and opcao in 'SN':
                # if opcao == 'S':
                #     return False
                # if opcao == 'N':
                #     return True
                return True if opcao == 'N' else False

        
    
    

        


print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 115
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

x = True
while x:
    opcao = menu()
    
    x = sair()

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
