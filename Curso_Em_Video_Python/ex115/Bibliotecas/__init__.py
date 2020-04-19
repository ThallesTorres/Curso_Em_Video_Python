
def linha():
    print('\033[33m', end='')
    print('-' * 40)
    print('\033[m', end='')
    

def titulo(msg='VAZIO'):
    print()
    linha()
    print(f'{msg.upper():^40}')
    linha()
    
    
def printERRO(msg='VAZIO', quebrar_linha=True):
    print(f'\033[31m--{msg}\033[m', 
          '\n' if quebrar_linha else '')
    
    
def printCONCLUIDO(msg='VAZIO'):
    print(f'\033[34m\n--{msg}\033[m', end='')
    

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
                return x
            
    
def ver():
    titulo('Pessoas cadastradas')
    
    try:
        with open('/home/fatality/Área de Trabalho/MegaNuvem/Projetos_GitHub/Curso_Em_Video_Python/Curso_Em_Video_Python/ex115/dados.txt', 'r') as dados:
            for linha in dados:
                print(linha, end='')
            
    except FileNotFoundError:
        printERRO('Não há pessoas cadastradas.', False)
    
    except Exception as erro:
        printERRO(f'Erro Inesperado.\n{erro.__class__}', False)
        
    finally:
        printCONCLUIDO('[ENTER] para continuar...')
        input()
            

def cadastrar():
    titulo('Cadastrar pessoa')

    with open('/home/fatality/Área de Trabalho/MegaNuvem/Projetos_GitHub/Curso_Em_Video_Python/Curso_Em_Video_Python/ex115/dados.txt', 'a') as dados:
        while True:
            try:
                nome = input('Nome: ').strip().title()
                
                if nome == '':
                    printERRO(f'Digite somente números.', False)
                    break

            except:
                printERRO(f'Erro Inesperado.\n{erro.__class__}', False)
                
            else:
                break
        
        while True:
            try:
                idade = int(input('Idade: '))

            except ValueError:
                printERRO(f'Digite somente números.', False)
            
            except Exception as erro:
                printERRO(f'Erro Inesperado.\n{erro.__class__}', False)
                
            else:
                break
            
        dados.write(f'{nome:<30} {idade} anos\n')
            
        printCONCLUIDO('Cadastro feito com sucesso!')
        printCONCLUIDO('[ENTER] para continuar...')
        input()
    
    
def sair():
    while True:
        try:
            print()
            opcao = input('\033[31mRealmente deseja SAIR? [S/N] \033[m').upper().strip()
            
        except Exception as erro:
            printERRO(f'Erro Inesperado.\n{erro.__class__}')
            
        else:
            if len(opcao) == 1 and opcao in 'SN':
                # if opcao == 'S':
                #     return False
                # if opcao == 'N':
                #     return True
                return True if opcao == 'N' else False
            
            else:
                printERRO('Erro, digite somente [S/N].')
