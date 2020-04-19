from lib.interface import *


def arquivo_existe(nome):
    try:
        with open(nome, 'rt') as x:
            pass 

    except FileNotFoundError:
        return False
    
    else:
        return True
    
    
def criar_arquivo(nome):
    try:
        with open(nome, 'wt+') as x:
            pass
        
    except:
        printRed('Erro na criação do arquivo!')

    else:
        print(f'Arquivo {nome} criado com sucesso!')
    
    
def ler_arquivo(nome):
    try:
        x = open(nome, 'rt')
    
    except:
        printRed('Erro ao ler o arquivo!')

    else:
        cabecalho('Pessoas cadastradas')
        
        for linha in x:
            dado = linha.replace('\n', '').split(';')
            print(f'{dado[0]:<30}{dado[1]} anos')
        
    finally:
        x.close()


def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        x = open(arquivo, 'at')

    except:
        printRed('Erro na abertura do arquivo!')

    else:
        try:
            x.write(f'{nome};{idade}\n')

        except:
            printRed('Erro ao escrever os dados!')

        else:
            print('\033[34mCadastrado com sucesso!\033[m')
        
    finally:
        x.close()
