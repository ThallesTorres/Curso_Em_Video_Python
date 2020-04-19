def printRed(msg):
    print(f"\033[31m--{msg}\033[m")


def leiaInt(msg):   
    while True:      
        try:
            num = int(input(msg))
            
        except (TypeError, ValueError):
            printRed("Tipo de dado digitado inválido.")
        
        except Exception as erro:
            printRed(f"Erro desconhecido.\n{erro.__class__}")
        
        else:
            return num
        
        finally:
            print()

def linha(tamanho=40):
    print('\033[33m', end='')
    print('-' * tamanho, '\033[m')


def cabecalho(txt='VAZIO'):
    linha()
    print(txt.upper().strip().center(40))
    linha()
    
    
def menu(lista=''):
    cabecalho('menu principal')

    for count, x in enumerate(lista):
        print(f'{count + 1} - {x}')
        
    linha()
    
    return leiaInt('Opção desejada: ')

