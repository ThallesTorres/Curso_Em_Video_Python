from lib.interface import *
from lib.arquivo import *
from time import sleep


arquivo = 'dados.txt'
if not arquivo_existe(arquivo):
    criar_arquivo(arquivo)

while True:
    opcao = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])

    if opcao == 1:
        ler_arquivo(arquivo)
        sleep(2)

    elif opcao == 2:
        cabecalho('Novo cadastro')
        nome = input('Nome: ').title()
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
        sleep(2)

    elif opcao == 3:
        cabecalho('saindo')
        sleep(2)
        break
        
    else:
        printRed('Erro! Digite somente 1, 2 ou 3.')
        sleep(2)

